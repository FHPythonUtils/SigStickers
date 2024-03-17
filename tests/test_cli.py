from __future__ import annotations

import sys
from pathlib import Path

THISDIR = Path(__file__).resolve().parent
PROJECT_DIR = THISDIR.parent
sys.path.insert(0, str(PROJECT_DIR))

from sigstickers.cli import main

cwd = THISDIR / "data"


def test_cli() -> None:
	assert (
		main(
			[
				"https://signal.art/addstickers/#pack_id=b676ec334ee2f771cadff5d095971e8c&pack_key=c957a57000626a2dc3cb69bf0e79c91c6b196b74d4d6ca1cbb830d3ad0ad4e36"
			],
			cwd=cwd,
		)
		== 0
	)
	assert len(list(Path(f"{cwd}/downloads/DonutTheDog/png").iterdir())) == 28


def test_cli_invalid_url() -> None:
	assert (
		main(
			[
				"https://signal.art/addstickers/#pack_key=c957a57000626a2dc3cb69bf0e79c91c6b196b74d4d6ca1cbb830d3ad0ad4e36"
			],
			cwd=cwd,
		)
		== 1
	)
