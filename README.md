[![GitHub top language](https://img.shields.io/github/languages/top/FHPythonUtils/SigStickers.svg?style=for-the-badge)](../../)
[![Codacy grade](https://img.shields.io/codacy/grade/[projid].svg?style=for-the-badge)](https://www.codacy.com/gh/FHPythonUtils/SigStickers)
[![Repository size](https://img.shields.io/github/repo-size/FHPythonUtils/SigStickers.svg?style=for-the-badge)](../../)
[![Issues](https://img.shields.io/github/issues/FHPythonUtils/SigStickers.svg?style=for-the-badge)](../../issues)
[![License](https://img.shields.io/github/license/FHPythonUtils/SigStickers.svg?style=for-the-badge)](/LICENSE.md)
[![Commit activity](https://img.shields.io/github/commit-activity/m/FHPythonUtils/SigStickers.svg?style=for-the-badge)](../../commits/master)
[![Last commit](https://img.shields.io/github/last-commit/FHPythonUtils/SigStickers.svg?style=for-the-badge)](../../commits/master)
[![PyPI Downloads](https://img.shields.io/pypi/dm/sigstickers.svg?style=for-the-badge)](https://pypi.org/project/sigstickers/)
[![PyPI Version](https://img.shields.io/pypi/v/sigstickers.svg?style=for-the-badge)](https://pypi.org/project/sigstickers/)

<!-- omit in TOC -->
# SigStickers - Signal Sticker Downloader

<img src="readme-assets/icons/name.png" alt="Project Icon" width="750">

Download sticker packs from Signal

- [Docs](#docs)
- [Using](#using)
- [Formats](#formats)
- [Install With PIP](#install-with-pip)
- [Language information](#language-information)
	- [Built for](#built-for)
- [Install Python on Windows](#install-python-on-windows)
	- [Chocolatey](#chocolatey)
	- [Download](#download)
- [Install Python on Linux](#install-python-on-linux)
	- [Apt](#apt)
- [How to run](#how-to-run)
	- [With VSCode](#with-vscode)
	- [From the Terminal](#from-the-terminal)
- [Download](#download-1)
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

## Docs
See the [Docs](/DOCS/README.md) for more information.


## Using

- Get the URL of the Signal sticker pack
- Run the program `python -m sigstickers`
- Enter the URL of the sticker pack
- Get the output in the `downloads` folder.


## Formats

|Format|Static|Animated|
|------|------|--------|
|.gif  |✔$    |✔$      |
|.png  |✔     |+       |
|.webp |✔     |✔       |

```txt
+ The first frame of an animated image is saved as gif
$ Some images saved as gif do not render as expected
```

## Install With PIP

```python
pip install sigstickers
```

Head to https://pypi.org/project/sigstickers/ for more info


## Language information
### Built for
This program has been written for Python 3 and has been tested with
Python version 3.9.0 <https://www.python.org/downloads/release/python-380/>.

## Install Python on Windows
### Chocolatey
```powershell
choco install python
```
### Download
To install Python, go to <https://www.python.org/> and download the latest
version.

## Install Python on Linux
### Apt
```bash
sudo apt install python3.9
```

## How to run
### With VSCode
1. Open the .py file in vscode
2. Ensure a python 3.9 interpreter is selected (Ctrl+Shift+P > Python:Select
Interpreter > Python 3.9)
3. Run by pressing Ctrl+F5 (if you are prompted to install any modules, accept)
### From the Terminal
```bash
./[file].py
```


## Download
### Clone
#### Using The Command Line
1. Press the Clone or download button in the top right
2. Copy the URL (link)
3. Open the command line and change directory to where you wish to
clone to
4. Type 'git clone' followed by URL in step 2
```bash
$ git clone https://github.com/FHPythonUtils/SigStickers
```

More information can be found at
<https://help.github.com/en/articles/cloning-a-repository>

#### Using GitHub Desktop
1. Press the Clone or download button in the top right
2. Click open in desktop
3. Choose the path for where you want and click Clone

More information can be found at
<https://help.github.com/en/desktop/contributing-to-projects/cloning-a-repository-from-github-to-github-desktop>

### Download Zip File

1. Download this GitHub repository
2. Extract the zip archive
3. Copy/ move to the desired location

## Community Files
### Licence
MIT License
(See the [LICENSE](/LICENSE.md) for more information.)

### Changelog
See the [Changelog](/CHANGELOG.md) for more information.

### Code of Conduct
In the interest of fostering an open and welcoming environment, we
as contributors and maintainers pledge to make participation in our
project and our community a harassment-free experience for everyone.
Please see the
[Code of Conduct](https://github.com/FHPythonUtils/.github/blob/master/CODE_OF_CONDUCT.md) for more information.

### Contributing
Contributions are welcome, please see the [Contributing Guidelines](https://github.com/FHPythonUtils/.github/blob/master/CONTRIBUTING.md) for more information.

### Security
Thank you for improving the security of the project, please see the [Security Policy](https://github.com/FHPythonUtils/.github/blob/master/SECURITY.md) for more information.