"""Download sticker packs from Signal
"""
import argparse
import asyncio

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
	packs = sum(args.pack, [])
	if packs is None:
		packs = []
		while True:
			name = input("Enter sticker_set url (leave blank to stop): ").strip()
			if name == "":
				break
			packs.append(name)
	for pack in packs:
		packAttrs = pack.split("#pack_id=")[-1].split("&pack_key=")
		asyncio.run(convertPack(*asyncio.run(downloadPack(*packAttrs))))


if __name__ == "__main__":
	cli()
