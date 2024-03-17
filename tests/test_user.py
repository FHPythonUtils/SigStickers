""" tests """
from __future__ import annotations

import asyncio
import sys
from pathlib import Path

THISDIR = Path(__file__).resolve().parent
PROJECT_DIR = THISDIR.parent
sys.path.insert(0, str(PROJECT_DIR))

from sigstickers import downloader

cwd = THISDIR / "data"

packs = [
	{
		"packId": "b676ec334ee2f771cadff5d095971e8c",
		"packKey": "c957a57000626a2dc3cb69bf0e79c91c6b196b74d4d6ca1cbb830d3ad0ad4e36",
		"len": 28,
	}
]


def test_downloadPack() -> None:
	swd, packName = asyncio.run(
		downloader.download_pack(packs[0]["packId"], packs[0]["packKey"], cwd)
	)
	assert swd.as_posix(), packName == (
		f"{cwd}/downloads/DonutTheDog",
		"DonutTheDog",
	)
	assert len(list(Path(f"{cwd}/downloads/DonutTheDog/webp").iterdir())) == packs[0]["len"]


def test_convertPack() -> None:
	swd, packName = asyncio.run(
		downloader.download_pack(packs[0]["packId"], packs[0]["packKey"], cwd)
	)
	asyncio.run(downloader.convert_pack(swd, packName, no_cache=True))
	assert len(list(Path(f"{cwd}/downloads/DonutTheDog/png").iterdir())) == packs[0]["len"]


def test_convertPack_cache() -> None:
	swd, packName = asyncio.run(
		downloader.download_pack(packs[0]["packId"], packs[0]["packKey"], cwd)
	)
	asyncio.run(downloader.convert_pack(swd, packName, no_cache=False))
	assert len(list(Path(f"{cwd}/downloads/DonutTheDog/png").iterdir())) == packs[0]["len"]
