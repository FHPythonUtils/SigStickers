# Downloader

[Sigstickers Index](../README.md#sigstickers-index) / [Sigstickers](./index.md#sigstickers) / Downloader

> Auto-generated documentation for [sigstickers.downloader](../../../sigstickers/downloader.py) module.

- [Downloader](#downloader)
  - [convertWithPIL](#convertwithpil)
  - [convert_pack](#convert_pack)
  - [download_pack](#download_pack)
  - [save_sticker](#save_sticker)

## convertWithPIL

[Show source in downloader.py:83](../../../sigstickers/downloader.py#L83)

Convert a webp file to png and gif.

#### Arguments

- `input_path` *Path* - path to the input image/ sticker
:param set[str] formats: set of formats

#### Returns

Type: *list[str]*
paths (as strings) of converted files

#### Signature

```python
def convertWithPIL(input_path: Path) -> list[str]: ...
```



## convert_pack

[Show source in downloader.py:112](../../../sigstickers/downloader.py#L112)

Convert the webp images into png and gif images.

#### Arguments

- `swd` *Path* - name of the directory to convert
- `pack_name` *Path* - name of the sticker pack (for cache + logging)
:param bool, optional no_cache: set to true to disable cache. Defaults to False.

#### Signature

```python
async def convert_pack(swd: Path, pack_name: Path, no_cache: bool = False) -> None: ...
```



## download_pack

[Show source in downloader.py:45](../../../sigstickers/downloader.py#L45)

Download a sticker pack.

#### Arguments

- `pack_id` *Path* - pack_id from url param. eg b676ec334ee2f771cadff5d095971e8c
- `pack_key` *Path* - pack_key from url param. eg
 c957a57000626a2dc3cb69bf0e79c91c6b196b74d4d6ca1cbb830d3ad0ad4e36
:param Path, optional cwd: set the current working directory

#### Returns

Type: *tuple[Path, Path]*
sticker working directory and pack title

#### Signature

```python
async def download_pack(
    pack_id: str, pack_key: str, cwd: Path = DEFAULT_CWD
) -> tuple[Path, Path]: ...
```

#### See also

- [DEFAULT_CWD](#default_cwd)



## save_sticker

[Show source in downloader.py:23](../../../sigstickers/downloader.py#L23)

Save a sticker.

#### Arguments

- `sticker` *Sticker* - the sticker object
- `path` *Path* - the path to write to

#### Returns

Type: *Path*
the filepath the file was written to

#### Signature

```python
def save_sticker(sticker: Sticker, path: Path) -> Path: ...
```