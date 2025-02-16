import shutil
from pathlib import Path
from typing import Generator

import pytest

from sigstickers.downloader import download_pack


@pytest.fixture
def test_data() -> Generator[Path, None, None]:
	test_dir = Path("test_data")
	yield test_dir
	shutil.rmtree(test_dir)


@pytest.mark.asyncio
async def test_download_pack(test_data: Path) -> None:
	pack_id = "b676ec334ee2f771cadff5d095971e8c"
	pack_key = "c957a57000626a2dc3cb69bf0e79c91c6b196b74d4d6ca1cbb830d3ad0ad4e36"
	sticker_dir, _pack_name = await download_pack(pack_id, pack_key, cwd=test_data)
	assert sticker_dir.exists()
	assert sticker_dir.is_dir()


@pytest.mark.asyncio
async def test_download_pack_bad_name(test_data: Path) -> None:
	pack_id = "4d92b5e3e92d1ac099830b17ac10793d"
	pack_key = "c8526aa2e25b911a405d39c1d4ee3977586e945550fddc33e1316626116da512"
	sticker_dir, _pack_name = await download_pack(pack_id, pack_key, cwd=test_data)
	assert sticker_dir.exists()
	assert sticker_dir.is_dir()
