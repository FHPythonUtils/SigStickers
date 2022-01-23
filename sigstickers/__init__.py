"""Download sticker packs from Signal
"""
from __future__ import annotations

import argparse
import asyncio
from sys import exit as sysexit
from urllib import parse

from .downloader import convertPack, downloadPack


def cli():
	"""cli entry point"""
	parser = argparse.ArgumentParser("Welcome to SigSticker, providing all of your sticker needs")
	parser.add_argument(
		"-p",
		"--pack",
		help="Pass in a pack url inline",
		nargs="+",
		action="append",
	)
	args = parser.parse_args()
	# Get the packs
	packs = sum(args.pack or [[]], [])
	if len(packs) == 0:
		packs = []
		while True:
			name = input("Enter sticker_set url (leave blank to stop): ").strip()
			if name == "":
				break
			packs.append(name)
	for pack in packs:
		packAttrs = parse.parse_qs(parse.urlparse(pack).fragment)
		if packAttrs.keys() < {"pack_id", "pack_key"}:
			print(
				"Sticker URLs need a pack_id and pack_key. Eg. https://signal.art/"
				"addstickers/#pack_id=9acc9e8aba563d26a4994e69263e3b25&"
				"pack_key=5a6dff3948c28efb9b7aaf93ecc375c69fc316e78077ed26867a14d10a0f6a12"
			)
			sysexit(1)
		asyncio.run(
			convertPack(
				*asyncio.run(
					downloadPack("".join(packAttrs["pack_id"]), "".join(packAttrs["pack_key"]))
				)
			)
		)


if __name__ == "__main__":
	cli()
