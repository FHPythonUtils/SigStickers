[![GitHub top language](https://img.shields.io/github/languages/top/FHPythonUtils/SigStickers.svg?style=for-the-badge&cacheSeconds=28800)](../../)
[![Issues](https://img.shields.io/github/issues/FHPythonUtils/SigStickers.svg?style=for-the-badge&cacheSeconds=28800)](../../issues)
[![License](https://img.shields.io/github/license/FHPythonUtils/SigStickers.svg?style=for-the-badge&cacheSeconds=28800)](/LICENSE.md)
[![Commit activity](https://img.shields.io/github/commit-activity/m/FHPythonUtils/SigStickers.svg?style=for-the-badge&cacheSeconds=28800)](../../commits/master)
[![Last commit](https://img.shields.io/github/last-commit/FHPythonUtils/SigStickers.svg?style=for-the-badge&cacheSeconds=28800)](../../commits/master)
[![PyPI Downloads](https://img.shields.io/pypi/dm/sigstickers.svg?style=for-the-badge&cacheSeconds=28800)](https://pypistats.org/packages/sigstickers)
[![PyPI Total Downloads](https://img.shields.io/badge/dynamic/json?style=for-the-badge&label=total%20downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi%2Epepy%2Etech%2Fapi%2Fv2%2Fprojects%2Fsigstickers)](https://pepy.tech/project/sigstickers)
[![PyPI Version](https://img.shields.io/pypi/v/sigstickers.svg?style=for-the-badge&cacheSeconds=28800)](https://pypi.org/project/sigstickers)

<!-- omit in toc -->
# SigStickers - Signal Sticker Downloader

<img src="readme-assets/icons/name.png" alt="Project Icon" width="750">

The `sigstickers` package provides functionality for downloading and converting sticker packs from https://signal.art/addstickers (find packs at https://www.sigstick.com/). Download stickers in WebP format, and convert them to PNG and GIF formats, with caching the converted stickers for faster retrieval.

- [Key Features](#key-features)
- [Using](#using)
- [Formats](#formats)
- [Documentation](#documentation)
- [Install With PIP](#install-with-pip)
- [Language information](#language-information)
	- [Built for](#built-for)
- [Install Python on Windows](#install-python-on-windows)
	- [Chocolatey](#chocolatey)
	- [Windows - Python.org](#windows---pythonorg)
- [Install Python on Linux](#install-python-on-linux)
	- [Apt](#apt)
	- [Dnf](#dnf)
- [Install Python on MacOS](#install-python-on-macos)
	- [Homebrew](#homebrew)
	- [MacOS - Python.org](#macos---pythonorg)
- [How to run](#how-to-run)
	- [Windows](#windows)
	- [Linux/ MacOS](#linux-macos)
- [Building](#building)
- [Testing](#testing)
- [Download Project](#download-project)
	- [Clone](#clone)
		- [Using The Command Line](#using-the-command-line)
		- [Using GitHub Desktop](#using-github-desktop)
	- [Download Zip File](#download-zip-file)
- [Community Files](#community-files)
	- [Licence](#licence)
	- [Changelog](#changelog)
	- [Code of Conduct](#code-of-conduct)
	- [Contributing](#contributing)
	- [Security](#security)
	- [Support](#support)
	- [Rationale](#rationale)

## Key Features

1. **Sticker Pack Downloading** from Signal from their https://signal.art/addstickers url
2. **Sticker Pack Conversion** from the WebP format to PNG and GIF formats, making them compatible with various platforms and applications.
3. **Caching Functionality** to store converted sticker images locally, reducing the need to re-convert them
4. **Asynchronous Processing** for downloading and converting sticker packs

## Using

1. Get the URL of the Signal sticker pack. In the form https://signal.art/addstickers (find packs at https://www.sigstick.com/)

2. Pass in multiple packs from the commandline with `-p/--pack`

	```bash
	$ python -m sigstickers --help
	usage: Welcome to SigSticker, providing all of your sticker needs [-h] [-p PACK [PACK ...]]

	options:
	-h, --help            show this help message and exit
	-p PACK [PACK ...], --pack PACK [PACK ...]
							Pass in a pack URL inline

	$ python -m sigstickers --pack 'https://signal.art/addstickers/#pack_id=b676ec334ee2f771cadff5d095971e8c&pack_key=c957a57000626a2dc3cb69bf0e79c91c6b196b74d4d6ca1cbb830d3ad0ad4e36'

	2024-03-17 00:14:16.354 | INFO     | sigstickers.downloader:download_pack:82 - ============================================================
	2024-03-17 00:14:16.805 | INFO     | sigstickers.downloader:download_pack:88 - Starting to scrape "DonutTheDog" ...
	2024-03-17 00:14:16.812 | INFO     | sigstickers.downloader:download_pack:89 - Time taken to scrape 28 stickers - 0.999s
	2024-03-17 00:14:16.813 | INFO     | sigstickers.downloader:download_pack:90 -
	2024-03-17 00:14:16.816 | INFO     | sigstickers.downloader:download_pack:96 - ------------------------------------------------------------
	2024-03-17 00:14:16.820 | INFO     | sigstickers.downloader:download_pack:97 - Starting download of "DonutTheDog" into ...\downloads\DonutTheDog
	2024-03-17 00:14:16.894 | INFO     | sigstickers.downloader:convert_pack:151 - ------------------------------------------------------------
	2024-03-17 00:14:16.897 | INFO     | sigstickers.caching:verify_converted:35 - -> Cache miss for DonutTheDog!
	2024-03-17 00:14:16.905 | INFO     | sigstickers.downloader:convert_pack:163 - Converting stickers "DonutTheDog"...
	2024-03-17 00:14:29.655 | INFO     | sigstickers.downloader:convert_pack:171 - Time taken to convert 28/28 stickers - 12.749s
	2024-03-17 00:14:29.656 | INFO     | sigstickers.downloader:convert_pack:175 -
	```

3. OR. Enter the URL of the sticker pack

	```bash
	$ python -m sigstickers
	Enter sticker_set URL (leave blank to stop): https://signal.art/addstickers/#pack_id=b676ec334ee2f771cadff5d095971e8c&pack_key=c957a57000626a2dc3cb69bf0e79c91c6b196b74d4d6ca1cbb830d3ad0ad4e36
	Enter sticker_set URL (leave blank to stop):
	2024-03-17 00:18:25.528 | INFO     | sigstickers.downloader:download_pack:82 - ============================================================
	2024-03-17 00:18:26.415 | INFO     | sigstickers.downloader:download_pack:88 - Starting to scrape "DonutTheDog" ...
	2024-03-17 00:18:26.417 | INFO     | sigstickers.downloader:download_pack:89 - Time taken to scrape 28 stickers - 0.885s
	2024-03-17 00:18:26.420 | INFO     | sigstickers.downloader:download_pack:90 -
	2024-03-17 00:18:26.426 | INFO     | sigstickers.downloader:download_pack:96 - ------------------------------------------------------------
	2024-03-17 00:18:26.428 | INFO     | sigstickers.downloader:download_pack:97 - Starting download of "DonutTheDog" into ...\downloads\DonutTheDog
	2024-03-17 00:18:26.497 | INFO     | sigstickers.downloader:convert_pack:151 - ------------------------------------------------------------
	2024-03-17 00:18:26.524 | INFO     | sigstickers.caching:verify_converted:33 - -> Cache hit for DonutTheDog!
	```

4. Get the output in the `downloads` folder.

	```powershell
	$ ls .\downloads\DonutTheDog\

	Mode                 LastWriteTime         Length Name
	----                 -------------         ------ ----
	d-----        17/03/2024     00꞉14                gif
	d-----        17/03/2024     00꞉14                png
	d-----        17/03/2024     00꞉08                webp

	$ ls .\downloads\DonutTheDog\webp

	Mode                 LastWriteTime         Length Name
	----                 -------------         ------ ----
	-a----        17/03/2024     00꞉18         285292 0+face_with_tears_of_joy+😂.webp
	-a----        17/03/2024     00꞉18         271726 1+face_blowing_a_kiss+😘.webp
	-a----        17/03/2024     00꞉18         306995 10+smiling_face_with_horns+😈.webp
	-a----        17/03/2024     00꞉18         293578 11+partying_face+🥳.webp
	-a----        17/03/2024     00꞉18         266627 12+angry_face+😠.webp
	```

## Formats

| Format | Static | Animated |
| ------ | ------ | -------- |
| .gif   | ✔$     | ✔$       |
| .png   | ✔      | +        |
| .webp  | ✔      | ✔        |

```txt
+ The first frame of an animated image is saved as png
$ Some images saved as gif do not render as expected
```

## Documentation

A high-level overview of how the documentation is organized organized will help you know
where to look for certain things:

<!--
- [Tutorials](/documentation/tutorials) take you by the hand through a series of steps to get
  started using the software. Start here if you’re new.
-->
- The [Technical Reference](/documentation/reference) documents APIs and other aspects of the
  machinery. This documentation describes how to use the classes and functions at a lower level
  and assume that you have a good high-level understanding of the software.
<!--
- The [Help](/documentation/help) guide provides a starting point and outlines common issues that you
  may have.
-->

## Install With PIP

```python
pip install sigstickers
```

Head to https://pypi.org/project/sigstickers/ for more info

## Language information

### Built for

This program has been written for Python versions 3.8 - 3.11 and has been tested with both 3.8 and
3.11

## Install Python on Windows

### Chocolatey

```powershell
choco install python
```

### Windows - Python.org

To install Python, go to https://www.python.org/downloads/windows/ and download the latest
version.

## Install Python on Linux

### Apt

```bash
sudo apt install python3.x
```

### Dnf

```bash
sudo dnf install python3.x
```

## Install Python on MacOS

### Homebrew

```bash
brew install python@3.x
```

### MacOS - Python.org

To install Python, go to https://www.python.org/downloads/macos/ and download the latest
version.

## How to run

### Windows

- Module
	`py -3.x -m [module]` or `[module]` (if module installs a script)

- File
	`py -3.x [file]` or `./[file]`

### Linux/ MacOS

- Module
	`python3.x -m [module]` or `[module]` (if module installs a script)

- File
	`python3.x [file]` or `./[file]`

## Building

This project uses https://github.com/FHPythonUtils/FHMake to automate most of the building. This
command generates the documentation, updates the requirements.txt and builds the library artefacts

Note the functionality provided by fhmake can be approximated by the following

```sh
handsdown  --cleanup -o documentation/reference
poetry export -f requirements.txt --output requirements.txt
poetry export -f requirements.txt --with dev --output requirements_optional.txt
poetry build
```

`fhmake audit` can be run to perform additional checks

## Testing

For testing with the version of python used by poetry use

```sh
poetry run pytest
```

Alternatively use `tox` to run tests over python 3.8 - 3.11

```sh
tox
```

## Download Project

### Clone

#### Using The Command Line

1. Press the Clone or download button in the top right
2. Copy the URL (link)
3. Open the command line and change directory to where you wish to
clone to
4. Type 'git clone' followed by URL in step 2

	```bash
	git clone https://github.com/FHPythonUtils/SigStickers
	```

More information can be found at
https://help.github.com/en/articles/cloning-a-repository

#### Using GitHub Desktop

1. Press the Clone or download button in the top right
2. Click open in desktop
3. Choose the path for where you want and click Clone

More information can be found at
https://help.github.com/en/desktop/contributing-to-projects/cloning-a-repository-from-github-to-github-desktop

### Download Zip File

1. Download this GitHub repository
2. Extract the zip archive
3. Copy/ move to the desired location

## Community Files

### Licence

MIT License
Copyright (c) FredHappyface
(See the [LICENSE](/LICENSE.md) for more information.)

### Changelog

See the [Changelog](/CHANGELOG.md) for more information.

### Code of Conduct

Online communities include people from many backgrounds. The *Project*
contributors are committed to providing a friendly, safe and welcoming
environment for all. Please see the
[Code of Conduct](https://github.com/FHPythonUtils/.github/blob/master/CODE_OF_CONDUCT.md)
 for more information.

### Contributing

Contributions are welcome, please see the
[Contributing Guidelines](https://github.com/FHPythonUtils/.github/blob/master/CONTRIBUTING.md)
for more information.

### Security

Thank you for improving the security of the project, please see the
[Security Policy](https://github.com/FHPythonUtils/.github/blob/master/SECURITY.md)
for more information.

### Support

Thank you for using this project, I hope it is of use to you. Please be aware that
those involved with the project often do so for fun along with other commitments
(such as work, family, etc). Please see the
[Support Policy](https://github.com/FHPythonUtils/.github/blob/master/SUPPORT.md)
for more information.

### Rationale

The rationale acts as a guide to various processes regarding projects such as
the versioning scheme and the programming styles used. Please see the
[Rationale](https://github.com/FHPythonUtils/.github/blob/master/RATIONALE.md)
for more information.
