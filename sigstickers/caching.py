"""Sticker caching functionality used by the downloader."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Callable

from loguru import logger

CACHE_DIR = Path(".cache")
if not CACHE_DIR.exists():
	CACHE_DIR.mkdir()


def verify_converted(pack_name: Path) -> bool:
	"""Verify the cache for a packName eg. "DonutTheDog". Uses the cache "version"
	to call the verify function for that version.

	Args:
	----
		pack_name (Path): name of the sticker pack eg. "DonutTheDog"

	Returns:
	-------
		bool: if the converted cache has been verified

	"""
	cache = CACHE_DIR / pack_name
	if cache.exists():
		data = json.loads(cache.read_text(encoding="utf-8"))
		verify_func = _get_verify_function(data.get("version", 1))
		if verify_func(data):
			logger.info(f"-> Cache hit for {pack_name}!")
			return True
	logger.info(f"-> Cache miss for {pack_name}!")
	return False


def _verify_converted_v1(data: dict[str, Any]) -> bool:
	"""Verify the cache for a packName using cache data.

	Args:
	----
		data (dict[Path, Any]): packName cache data to verify

	Returns:
	-------
		bool: if the converted cache has been verified

	"""
	swd = data.get("info", {}).get("swd")
	if swd:
		png_dir = Path(swd) / "png"
		return png_dir.exists() and data["converted"]["converted"] == data["converted"]["total"]
	return False


def _verify_converted_v2(data: dict[str, Any]) -> bool:
	"""Verify the cache for a packName using cache data.

	Args:
	----
		data (dict[Path, Any]): packName cache data to verify

	Returns:
	-------
		bool: if the converted cache has been verified

	"""
	webp_files: list[str] = data.get("webp_files", [])
	converted_files: list[list[str]] = data.get("converted_files", [])

	if len(webp_files) != len(converted_files):
		return False

	for x in webp_files + [item for sublist in converted_files for item in sublist]:
		if not Path(x).is_file():
			return False
	return True


def create_converted(pack_name: Path, data: dict) -> None:
	"""Write cache data to a file identified by packName.

	Args:
	----
		pack_name (Path): name of the sticker pack eg. "DonutTheDog"
		data (dict): packName cache data to write to cache

	"""
	cache = CACHE_DIR / pack_name
	cache.write_text(json.dumps(data), encoding="utf-8")


def _get_verify_function(version: int) -> Callable[[dict[str, Any]], bool]:
	"""Get the appropriate cache verification function based on version.

	Args:
	----
		version (int): Cache version

	Returns:
	-------
		Callable[[dict[str, Any]], bool]: Cache verification function

	"""
	return {
		1: _verify_converted_v1,
		2: _verify_converted_v2,
	}.get(version, _verify_converted_v1)
