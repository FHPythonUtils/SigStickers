# downloader

> Auto-generated documentation for [sigstickers.downloader](../../sigstickers/downloader.py) module.

- [Sigstickers](../README.md#sigstickers-index) / [Modules](../README.md#sigstickers-modules) / [sigstickers](index.md#sigstickers) / downloader
    - [assureDirExists](#assuredirexists)
    - [convertPack](#convertpack)
    - [downloadPack](#downloadpack)

## assureDirExists

[[find in source code]](../../sigstickers/downloader.py#L12)

```python
def assureDirExists(directory: str, root: str) -> str:
```

make the dir if not exists

#### Arguments

- `dir` *str* - the directory name
- `root` *str* - the path of the root directory

#### Returns

- `str` - the full path

## convertPack

[[find in source code]](../../sigstickers/downloader.py#L58)

```python
async def convertPack(swd: str, packTitle: str):
```

## downloadPack

[[find in source code]](../../sigstickers/downloader.py#L28)

```python
async def downloadPack(packId, packKey):
```
