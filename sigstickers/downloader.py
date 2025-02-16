"""Sticker download and convert functions used by the module entry point."""

from __future__ import annotations

import re
import time
import unicodedata
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from emoji import demojize
from loguru import logger
from PIL import Image
from signalstickers_client import StickersClient
from signalstickers_client.models.sticker import Sticker

from sigstickers.caching import create_converted, verify_converted

UNKNOWN = "🤷‍♂️"
DEFAULT_CWD = Path.cwd()


def save_sticker(sticker: Sticker, path: Path) -> Path:
	"""Save a sticker.

	:param Sticker sticker: the sticker object
	:param Path path: the path to write to

	:return Path: the filepath the file was written to

	"""
	sticker_emoji = sticker.emoji or UNKNOWN
	file_path = path / f"{sticker.id}+{demojize(sticker_emoji)[1:-1]}+{sticker_emoji}.webp"
	file_path.write_bytes(sticker.image_data or b"")
	return file_path


def _sanitize_filename(filename: str) -> str:
	sanitized_filename = re.sub(r"[^\w\s.-]", "_", filename)
	sanitized_filename = re.sub(r"\s+", "_", sanitized_filename)
	sanitized_filename = sanitized_filename.strip(" .")
	return unicodedata.normalize("NFKD", sanitized_filename).encode("ascii", "ignore").decode()


async def download_pack(pack_id: str, pack_key: str, cwd: Path = DEFAULT_CWD) -> tuple[Path, Path]:
	"""Download a sticker pack.

	:param Path pack_id: pack_id from url param. eg b676ec334ee2f771cadff5d095971e8c
	:param Path pack_key: pack_key from url param. eg
		c957a57000626a2dc3cb69bf0e79c91c6b196b74d4d6ca1cbb830d3ad0ad4e36
	:param Path, optional cwd: set the current working directory

	:return tuple[Path, Path]: sticker working directory and pack title

	"""
	logger.info("=" * 60)
	start = time.time()
	async with StickersClient() as client:
		pack = await client.get_pack(pack_id, pack_key)
		pack_name = Path(_sanitize_filename(pack.title or UNKNOWN))
		end = time.time()
		logger.info(f'Starting to scrape "{pack_name}" ...')
		logger.info(f"Time taken to scrape {pack.nb_stickers} stickers - {end - start:.3f}s")
		logger.info("")

	swd = cwd / "downloads" / pack_name
	swd.mkdir(parents=True, exist_ok=True)
	webp_dir = swd / "webp"
	webp_dir.mkdir(parents=True, exist_ok=True)

	# Save the stickers
	logger.info("-" * 60)
	logger.info(f'Starting download of "{pack_name}" into {swd}')
	with ThreadPoolExecutor(max_workers=4) as executor:
		for i in as_completed(
			[executor.submit(save_sticker, sticker, webp_dir) for sticker in pack.stickers]
		):
			i.result()

	return swd, pack_name


def convertWithPIL(input_path: Path) -> list[str]:
	"""Convert a webp file to png and gif.

	:param Path input_path: path to the input image/ sticker
	:param set[str] formats: set of formats
	:return list[str]: paths (as strings) of converted files
	"""

	input_file = input_path.as_posix()

	img = Image.open(input_file)
	png_file = input_file.replace("webp", "png")
	gif_file = input_file.replace("webp", "gif")
	img.save(png_file)

	try:
		img.save(
			gif_file,
			version="GIF89a",
			disposal=2,
			save_all=True,
			loop=0,
		)
	except ValueError:
		logger.error(f"Failed to save {input_file} as gif")
		return [png_file]
	return [png_file, gif_file]


async def convert_pack(
	swd: Path,
	pack_name: Path,
	*,
	no_cache: bool = False,
) -> None:
	"""Convert the webp images into png and gif images.

	:param Path swd: name of the directory to convert
	:param Path pack_name: name of the sticker pack (for cache + logging)
	:param bool, optional no_cache: set to true to disable cache. Defaults to False.
	"""
	logger.info("-" * 60)
	if not no_cache and verify_converted(pack_name):
		return

	(swd / "png").mkdir(parents=True, exist_ok=True)
	(swd / "gif").mkdir(parents=True, exist_ok=True)

	webp_files = [file for file in (swd / "webp").iterdir() if file.is_file()]

	# Convert stickers
	start = time.time()
	logger.info(f'Converting stickers for "{pack_name}"...')
	converted_files = []
	with ThreadPoolExecutor(max_workers=4) as executor:
		for converted in as_completed(
			[executor.submit(convertWithPIL, sticker) for sticker in webp_files]
		):
			converted_files.extend(converted.result())
	end = time.time()
	logger.info(
		f"Time taken to convert {len(converted_files)}/{len(webp_files)} "
		f"stickers - {end - start:.3f}s"
	)

	logger.info("")
	create_converted(
		pack_name,
		data={
			"version": 2,
			"converted_files": converted_files,
			"webp_files": _files_to_str(webp_files),
		},
	)


def _files_to_str(files: list[Path]) -> list[str]:
	return [x.absolute().as_posix() for x in files]
