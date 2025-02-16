# Caching

[Sigstickers Index](../README.md#sigstickers-index) / [Sigstickers](./index.md#sigstickers) / Caching

> Auto-generated documentation for [sigstickers.caching](../../../sigstickers/caching.py) module.

- [Caching](#caching)
  - [_get_verify_function](#_get_verify_function)
  - [_verify_converted_v1](#_verify_converted_v1)
  - [_verify_converted_v2](#_verify_converted_v2)
  - [create_converted](#create_converted)
  - [verify_converted](#verify_converted)

## _get_verify_function

[Show source in caching.py:79](../../../sigstickers/caching.py#L79)

Get the appropriate cache verification function based on version.

#### Arguments

- `version` *int* - Cache version

#### Returns

Type: *Callable[[dict[str, Any]], bool]*
Cache verification function

#### Signature

```python
def _get_verify_function(version: int) -> Callable[[dict[str, Any]], bool]: ...
```



## _verify_converted_v1

[Show source in caching.py:35](../../../sigstickers/caching.py#L35)

Verify the cache for a packName using cache data.

:param dict[Path, Any] data: packName cache data to verify

#### Returns

Type: *bool*
if the converted cache has been verified

#### Signature

```python
def _verify_converted_v1(data: dict[str, Any]) -> bool: ...
```



## _verify_converted_v2

[Show source in caching.py:49](../../../sigstickers/caching.py#L49)

Verify the cache for a packName using cache data.

:param dict[Path, Any] data: packName cache data to verify

#### Returns

Type: *bool*
if the converted cache has been verified

#### Signature

```python
def _verify_converted_v2(data: dict[str, Any]) -> bool: ...
```



## create_converted

[Show source in caching.py:68](../../../sigstickers/caching.py#L68)

Write cache data to a file identified by packName.

#### Arguments

- `pack_name` *Path* - name of the sticker pack eg. "DonutTheDog"
- `data` *dict* - packName cache data to write to cache

#### Signature

```python
def create_converted(pack_name: Path, data: dict) -> None: ...
```



## verify_converted

[Show source in caching.py:16](../../../sigstickers/caching.py#L16)

Verify the cache for a packName eg. "DonutTheDog". Uses the cache "version"
to call the verify function for that version.

#### Arguments

- `pack_name` *Path* - name of the sticker pack eg. "DonutTheDog"

#### Returns

Type: *bool*
if the converted cache has been verified

#### Signature

```python
def verify_converted(pack_name: Path) -> bool: ...
```