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


def assure_dir_exists(*parts: Path | str) -> Path:
	"""Make the directory if it does not exist.

	Args:
	----
		parts (Path): path parts

	Returns:
	-------
		Path: the full path

	"""
	full_path = Path(*parts)
	full_path.mkdir(parents=True, exist_ok=True)
	return full_path


def save_sticker(sticker: Sticker, path: Path) -> Path:
	"""Save a sticker.

	Args:
	----
		sticker (Sticker): the sticker object
		path (Path): the path to write to

	Returns:
	-------
		Path: the filepath the file was written to

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

	Args:
	----
		pack_id (Path): pack_id from url param. eg b676ec334ee2f771cadff5d095971e8c
		pack_key (Path): pack_key from url param. eg
		c957a57000626a2dc3cb69bf0e79c91c6b196b74d4d6ca1cbb830d3ad0ad4e36
		cwd (Path, optional): set the current working directory

	Returns:
	-------
		tuple[Path, Path]: sticker working directory and pack title

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

	swd = assure_dir_exists(cwd, "downloads", pack_name)
	webp_dir = assure_dir_exists(swd, "webp")

	# Save the stickers
	logger.info("-" * 60)
	logger.info(f'Starting download of "{pack_name}" into {swd}')
	with ThreadPoolExecutor(max_workers=4) as executor:
		for i in as_completed(
			[executor.submit(save_sticker, sticker, webp_dir) for sticker in pack.stickers]
		):
			i.result()

	return swd, pack_name


def convert_with_pil(input_path: Path) -> list[str]:
	"""Convert the webp file to png.

	Args:
	----
		input_path (Path): path to input file

	Returns:
	-------
		Path: path to input file

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


async def convert_pack(swd: Path, pack_name: Path, *, no_cache: bool = False) -> None:
	"""Convert the webp images into png and gif images.

	Args:
	----
		swd (Path): name of the directory to convert
		pack_name (Path): name of the sticker pack (for cache + logging)
		no_cache (bool, optional): set to true to disable cache. Defaults to False.

	"""
	logger.info("-" * 60)
	if not no_cache and verify_converted(pack_name):
		return

	webp_dir = assure_dir_exists(swd, "webp")
	assure_dir_exists(swd, "png")
	assure_dir_exists(swd, "gif")

	webp_files = [file for file in webp_dir.iterdir() if file.is_file()]

	# Convert stickers
	start = time.time()
	logger.info(f'Converting stickers for "{pack_name}"...')
	converted_files = []
	with ThreadPoolExecutor(max_workers=4) as executor:
		for converted in as_completed(
			[executor.submit(convert_with_pil, sticker) for sticker in webp_files]
		):
			converted_files.append(converted.result())
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
	return [str(x.absolute()) for x in files]
