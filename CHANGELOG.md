# Changelog

All major and minor version changes will be documented in this file. Details of
patch-level version changes can be found in [commit messages](../../commits/master).

## 2022.1.1 - 2022/06/25

- Fix: use `os.makedirs` instead of `os.mkdir`
- Update pre-commit

## 2022.1 - 2022/04/11

- Tests and code improvements
- Update pre-commit

## 2022 - 2022/01/23

- Improvements to saving gifs
- Bump pillow version (CVE-2022-22815, CVE-2022-22816, CVE-2022-22817)
- Use urllib.parse to parse urls in place of string splitting

## 2021.2.3 - 2021/12/10

- Fix https://github.com/FHPythonUtils/SigStickers/issues/1
- More meaningful error messages

## 2021.2.1 - 2021/10/08

- Implement action='extend' for pre 3.7 eg. `python3 -m sigstickers -p pack1 pack2 -p pack3`

## 2021.2 - 2021/10/04

- Added caching functionality - output cache hit/miss to stdout for converter
- refactored code

## 2021.1 - 2021/01/19

- File names are now the emoji as text followed by the emoji glyph e.g.
  "0+smiling_face_with_3_hearts+🥰" followed by the file extension
  (requires `emoji` for this)
- Strings double-quoted

## 2021.0.1 - 2021/01/13

- Improvements to gifs
- Animations supported in gifs
- Bugfixes

## 2021 - 2021/01/13

- First release
- Similar UI to `tstickers`
- Gifs seem to look horrible
