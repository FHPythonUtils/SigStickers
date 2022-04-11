# Downloader

> Auto-generated documentation for [sigstickers.downloader](../../../sigstickers/downloader.py) module.

Sticker download and convert functions used by the module entry point.

- [Sigstickers](../README.md#sigstickers-index) / [Modules](../MODULES.md#sigstickers-modules) / [Sigstickers](index.md#sigstickers) / Downloader
    - [assureDirExists](#assuredirexists)
    - [convertPack](#convertpack)
    - [convertWithPIL](#convertwithpil)
    - [downloadPack](#downloadpack)
    - [saveSticker](#savesticker)

## assureDirExists

[[find in source code]](../../../sigstickers/downloader.py#L19)

```python
def assureDirExists(directory: str, root: str) -> str:
```

Make the dir if not exists

#### Arguments

- `directory` *str* - the directory name
- `root` *str* - the path of the root directory

#### Returns

- `str` - the full path

## convertPack

[[find in source code]](../../../sigstickers/downloader.py#L115)

```python
async def convertPack(swd: str, packName: str, noCache=False):
```

Convert the webp images into png and gif images

#### Arguments

- `swd` *str* - name of the directory to convert
- `packName` *str* - name of the sticker pack (for cache + logging)
- `noCache` *bool, optional* - set to true to disable cache. Defaults to False.

## convertWithPIL

[[find in source code]](../../../sigstickers/downloader.py#L94)

```python
def convertWithPIL(inputFile: str) -> str:
```

Convert the webp file to png

#### Arguments

- `inputFile` *str* - path to input file

#### Returns

- `str` - path to input file

## downloadPack

[[find in source code]](../../../sigstickers/downloader.py#L57)

```python
async def downloadPack(
    packId: str,
    packKey: str,
    cwd: str = os.getcwd(),
) -> tuple[str, str]:
```

Download a sticker pack.

#### Arguments

- `packId` *str* - pack_id from url param. eg b676ec334ee2f771cadff5d095971e8c
- `packKey` *str* - pack_key from url param. eg
c957a57000626a2dc3cb69bf0e79c91c6b196b74d4d6ca1cbb830d3ad0ad4e36
- `cwd` *str, optional* - set the current working directory

#### Returns

- `tuple[str,` *str]* - sticker working directory and pack title

## saveSticker

[[find in source code]](../../../sigstickers/downloader.py#L38)

```python
def saveSticker(sticker: Sticker, path: str) -> str:
```

Save a sticker

#### Arguments

- `sticker` *Sticker* - the sticker object
- `path` *str* - the path to write to

#### Returns

- `str` - the filepath the file was written to
