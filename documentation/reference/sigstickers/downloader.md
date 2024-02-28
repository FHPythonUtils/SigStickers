# Downloader

[Sigstickers Index](../README.md#sigstickers-index) / [Sigstickers](./index.md#sigstickers) / Downloader

> Auto-generated documentation for [sigstickers.downloader](../../../sigstickers/downloader.py) module.

- [Downloader](#downloader)
  - [assureDirExists](#assuredirexists)
  - [convertPack](#convertpack)
  - [convertWithPIL](#convertwithpil)
  - [downloadPack](#downloadpack)
  - [saveSticker](#savesticker)

## assureDirExists

[Show source in downloader.py:19](../../../sigstickers/downloader.py#L19)

Make the dir if not exists

#### Arguments

- `directory` *str* - the directory name
- `root` *str* - the path of the root directory

#### Returns

- `str` - the full path

#### Signature

```python
def assureDirExists(directory: str, root: str) -> str: ...
```



## convertPack

[Show source in downloader.py:121](../../../sigstickers/downloader.py#L121)

Convert the webp images into png and gif images

#### Arguments

- `swd` *str* - name of the directory to convert
- `packName` *str* - name of the sticker pack (for cache + logging)
- `noCache` *bool, optional* - set to true to disable cache. Defaults to False.

#### Signature

```python
async def convertPack(swd: str, packName: str, noCache=False): ...
```



## convertWithPIL

[Show source in downloader.py:96](../../../sigstickers/downloader.py#L96)

Convert the webp file to png

#### Arguments

- `inputFile` *str* - path to input file

#### Returns

- `str` - path to input file

#### Signature

```python
def convertWithPIL(inputFile: str) -> str: ...
```



## downloadPack

[Show source in downloader.py:54](../../../sigstickers/downloader.py#L54)

Download a sticker pack.

#### Arguments

- `packId` *str* - pack_id from url param. eg b676ec334ee2f771cadff5d095971e8c
- `packKey` *str* - pack_key from url param. eg
c957a57000626a2dc3cb69bf0e79c91c6b196b74d4d6ca1cbb830d3ad0ad4e36
- `cwd` *str, optional* - set the current working directory

#### Returns

- `tuple[str,` *str]* - sticker working directory and pack title

#### Signature

```python
async def downloadPack(
    packId: str, packKey: str, cwd: str = os.getcwd()
) -> tuple[str, str]: ...
```



## saveSticker

[Show source in downloader.py:35](../../../sigstickers/downloader.py#L35)

Save a sticker

#### Arguments

- `sticker` *Sticker* - the sticker object
- `path` *str* - the path to write to

#### Returns

- `str` - the filepath the file was written to

#### Signature

```python
def saveSticker(sticker: Sticker, path: str) -> str: ...
```