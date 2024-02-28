""" tests """
from __future__ import annotations

import asyncio
import sys
from pathlib import Path

THISDIR = str(Path(__file__).resolve().parent)
PROJECT_DIR = Path(THISDIR).parent
sys.path.insert(0, str(PROJECT_DIR))

from sigstickers import downloader

cwd = f"{THISDIR}/data"

packs = [
	{
		"packId": "b676ec334ee2f771cadff5d095971e8c",
		"packKey": "c957a57000626a2dc3cb69bf0e79c91c6b196b74d4d6ca1cbb830d3ad0ad4e36",
		"len": 28,
	}
]


def test_downloadPack():
	swd, packName = asyncio.run(
		downloader.downloadPack(packs[0]["packId"], packs[0]["packKey"], cwd)
	)
	assert swd.replace("\\", "/"), packName == (
		f"{cwd}/downloads/DonutTheDog",
		"DonutTheDog",
	)
	assert (
		len(list(Path(f"{cwd}/downloads/DonutTheDog/webp").iterdir()))
		== packs[0]["len"]
	)


def test_convertPack():
	swd, packName = asyncio.run(
		downloader.downloadPack(packs[0]["packId"], packs[0]["packKey"], cwd)
	)
	asyncio.run(downloader.convertPack(swd, packName, noCache=True))
	assert (
		len(list(Path(f"{cwd}/downloads/DonutTheDog/png").iterdir())) == packs[0]["len"]
	)
