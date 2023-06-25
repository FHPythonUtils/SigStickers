# Caching

[Sigstickers Index](../README.md#sigstickers-index) /
[Sigstickers](./index.md#sigstickers) /
Caching

> Auto-generated documentation for [sigstickers.caching](../../../sigstickers/caching.py) module.

- [Caching](#caching)
  - [createConverted](#createconverted)
  - [verifyConverted](#verifyconverted)

## createConverted

[Show source in caching.py:52](../../../sigstickers/caching.py#L52)

Write cache data to a file identified by packName

#### Arguments

- `packName` *str* - name of the sticker pack eg. "DonutTheDog"
- `data` *dict* - packName cache data to write to cache

#### Signature

```python
def createConverted(packName: str, data: dict):
    ...
```



## verifyConverted

[Show source in caching.py:14](../../../sigstickers/caching.py#L14)

Verify the cache for a packName eg. "DonutTheDog". Uses the cache "version"
to call the verify function for that version

#### Arguments

- `packName` *str* - name of the sticker pack eg. "DonutTheDog"

#### Returns

- `bool` - if the converted cache has been verified

#### Signature

```python
def verifyConverted(packName: str) -> bool:
    ...
```


