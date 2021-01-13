from __future__ import annotations
"""Provides the module functions
"""
import os
import time
import anyio
from PIL import Image
from signalstickers_client import StickersClient

opj = os.path.join

def assureDirExists(directory: str, root: str) -> str:
	"""make the dir if not exists
	Args:
		dir (str): the directory name
		root (str): the path of the root directory
	Returns:
		str: the full path
	"""
	fullPath = opj(root, directory)
	if os.path.isdir(fullPath):
		pass
	else:
		os.mkdir(fullPath)

	return fullPath

async def downloadPack(packId, packKey):
	print('=' * 60)
	start = time.time()
	async with StickersClient() as client:
		pack = await client.get_pack(packId, packKey)
		end  = time.time()
		print(f"Starting to scrape \"{pack.title}\" ...")
		print('Time taken to scrape {} stickers - {:.3f}s'.format(pack.nb_stickers, end - start))
		print()

	async def saveSticker(sticker):
		async with await anyio.open_file(
			opj(webpDir, "{}.webp".format(sticker.id)),
			"wb",
		) as file:
			await file.write(sticker.image_data)

	async def convertStatic(inputFile: str):
		"""Convert the webp file to png
		Args:
			inputFile (str): path to input file
		Returns:
			None
		"""
		img = Image.open(inputFile)
		img.save(inputFile.replace("webp", "png"))
		try:
			img.save(
			inputFile.replace("webp", "gif"))
		except ValueError:
			print("Failed to save {} as gif".format(inputFile))

	async with anyio.create_task_group() as taskGroup:
		cwd = assureDirExists('downloads', root=os.getcwd())
		swd = assureDirExists(pack.title, root=cwd)
		webpDir = assureDirExists('webp', root=swd)
		assureDirExists('png', root=swd)
		assureDirExists('gif', root=swd)
		# Save the stickers
		print('-' * 60)
		start = time.time()
		for sticker in pack.stickers:
			await taskGroup.spawn(saveSticker, sticker)
		end  = time.time()
		print(f"Starting download of \"{pack.title}\" into {swd}")
		print()
		# Convert the stickers
		staticStickers = [opj(webpDir, i) for i in os.listdir(webpDir)
		if i.endswith(".webp")] # yapf: disable
		print('-' * 60)
		start = time.time()
		for sticker in staticStickers:
			await taskGroup.spawn(convertStatic, sticker)
		end  = time.time()
		print(f"Starting conversion of \"{pack.title}\" into {swd}")
		print()
