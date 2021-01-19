"""Download sticker packs from Signal
"""
import argparse
import anyio
from sigstickers.downloader import downloadPack, convertPack


def cli():
	""" cli entry point """
	parser = argparse.ArgumentParser("Welcome to SigSticker, providing all of your sticker needs")
	parser.add_argument("-p", "--pack", help="Pass in a pack url inline", action="append")
	args = parser.parse_args()
	# Get the packs
	names = args.pack
	if names is None:
		names = []
		while True:
			name = input("Enter sticker_set url (leave blank to stop): ").strip()
			if name == "":
				break
			names.append(name)
	names = [name.split("#pack_id=")[-1].split("&pack_key=") for name in names]
	stickerAttrs = []
	for sset in names:
		stickerAttrs.append(anyio.run(downloadPack, sset[0], sset[1]))
	for index, sset in enumerate(names):
		anyio.run(convertPack, *stickerAttrs[index])


if __name__ == "__main__":
	cli()
