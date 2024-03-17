# Downloader

[Sigstickers Index](../README.md#sigstickers-index) / [Sigstickers](./index.md#sigstickers) / Downloader

> Auto-generated documentation for [sigstickers.downloader](../../../sigstickers/downloader.py) module.

- [Downloader](#downloader)
  - [assure_dir_exists](#assure_dir_exists)
  - [convert_pack](#convert_pack)
  - [convert_with_pil](#convert_with_pil)
  - [download_pack](#download_pack)
  - [files_to_str](#files_to_str)
  - [save_sticker](#save_sticker)

## assure_dir_exists

[Show source in downloader.py:21](../../../sigstickers/downloader.py#L21)

Make the directory if it does not exist.

#### Arguments

----
 - `parts` *Path* - path parts

#### Returns

-------
 - `Path` - the full path

#### Signature

```python
def assure_dir_exists(*parts: Path | str) -> Path: ...
```



## convert_pack

[Show source in downloader.py:141](../../../sigstickers/downloader.py#L141)

Convert the webp images into png and gif images.

#### Arguments

----
 - `swd` *Path* - name of the directory to convert
 - `pack_name` *Path* - name of the sticker pack (for cache + logging)
 - `no_cache` *bool, optional* - set to true to disable cache. Defaults to False.

#### Signature

```python
async def convert_pack(swd: Path, pack_name: Path, no_cache=False): ...
```



## convert_with_pil

[Show source in downloader.py:107](../../../sigstickers/downloader.py#L107)

Convert the webp file to png.

#### Arguments

----
 - `input_path` *Path* - path to input file

#### Returns

-------
 - `Path` - path to input file

#### Signature

```python
def convert_with_pil(input_path: Path) -> list[str]: ...
```



## download_pack

[Show source in downloader.py:67](../../../sigstickers/downloader.py#L67)

Download a sticker pack.

#### Arguments

----
 - `pack_id` *Path* - pack_id from url param. eg b676ec334ee2f771cadff5d095971e8c
 - `pack_key` *Path* - pack_key from url param. eg
 c957a57000626a2dc3cb69bf0e79c91c6b196b74d4d6ca1cbb830d3ad0ad4e36
 - `cwd` *Path, optional* - set the current working directory

#### Returns

-------
 - `tuple[Path,` *Path]* - sticker working directory and pack title

#### Signature

```python
async def download_pack(
    pack_id: str, pack_key: str, cwd: Path = Path.cwd()
) -> tuple[Path, Path]: ...
```



## files_to_str

[Show source in downloader.py:186](../../../sigstickers/downloader.py#L186)

#### Signature

```python
def files_to_str(files: list[Path]) -> list[str]: ...
```



## save_sticker

[Show source in downloader.py:38](../../../sigstickers/downloader.py#L38)

Save a sticker.

#### Arguments

----
 - `sticker` *Sticker* - the sticker object
 - `path` *Path* - the path to write to

#### Returns

-------
 - `Path` - the filepath the file was written to

#### Signature

```python
def save_sticker(sticker: Sticker, path: Path) -> Path: ...
```