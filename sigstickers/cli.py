"""Download sticker packs from Signal."""
from __future__ import annotations

import argparse
import asyncio
import functools
import operator
from pathlib import Path
from sys import exit as sysexit
from urllib import parse

from loguru import logger

from sigstickers.downloader import DEFAULT_CWD, convert_pack, download_pack


def cli() -> None:  # pragma: no cover
	"""CLI entry point."""
	parser = argparse.ArgumentParser("Welcome to SigSticker, providing all of your sticker needs")
	parser.add_argument(
		"-p",
		"--pack",
		help="Pass in a pack URL inline",
		nargs="+",
		action="append",
	)
	args = parser.parse_args()
	# Get the packs
	packs: list[str] = functools.reduce(operator.iadd, args.pack or [[]], [])
	if not packs:
		packs = []
		while True:
			name = input("Enter sticker_set URL (leave blank to stop): ").strip()
			if not name:
				break
			packs.append(name)
	sysexit(main(packs))


def main(packs: list[str], cwd: Path = DEFAULT_CWD) -> int:
	"""Download, and convert sticker packs."""
	for pack in packs:
		pack_attrs: dict[str, list[str]] = parse.parse_qs(parse.urlparse(pack).fragment)
		if {"pack_id", "pack_key"} > pack_attrs.keys():
			logger.error(
				"Sticker URLs need a pack_id and pack_key. Eg. https://signal.art/"
				"addstickers/#pack_id=9acc9e8aba563d26a4994e69263e3b25&"
				"pack_key=5a6dff3948c28efb9b7aaf93ecc375c69fc316e78077ed26867a14d10a0f6a12"
			)
			return 1

		downloaded = asyncio.run(
			download_pack("".join(pack_attrs["pack_id"]), "".join(pack_attrs["pack_key"]), cwd=cwd)
		)

		asyncio.run(convert_pack(*downloaded))
	return 0
