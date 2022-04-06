# Caching

> Auto-generated documentation for [sigstickers.caching](../../../sigstickers/caching.py) module.

Sticker caching functionality used by the downloader.

- [Sigstickers](../README.md#sigstickers-index) / [Modules](../MODULES.md#sigstickers-modules) / [Sigstickers](index.md#sigstickers) / Caching
    - [createConverted](#createconverted)
    - [verifyConverted](#verifyconverted)

## createConverted

[[find in source code]](../../../sigstickers/caching.py#L52)

```python
def createConverted(packName: str, data: dict):
```

Write cache data to a file identified by packName

#### Arguments

- `packName` *str* - name of the sticker pack eg. "DonutTheDog"
- `data` *dict* - packName cache data to write to cache

## verifyConverted

[[find in source code]](../../../sigstickers/caching.py#L14)

```python
def verifyConverted(packName: str) -> bool:
```

Verify the cache for a packName eg. "DonutTheDog". Uses the cache "version"
to call the verify function for that version

#### Arguments

- `packName` *str* - name of the sticker pack eg. "DonutTheDog"

#### Returns

- `bool` - if the converted cache has been verified
