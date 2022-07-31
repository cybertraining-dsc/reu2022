# Windows Configuration

## Install WSL with Ubuntu 22.04

To install the Windows Subsystem for Linux
(WSL), run the following command in an
administrator PowerShell:

```bash
wsl --install
```

## Install Chocolatey

To install chocolatey, follow the tutorial
at <https://github.com/cybertraining-dsc/cybertraining-dsc.github.io/blob/main/content/en/docs/tutorial/reu/chocolatey/index.md>

## Install Git Bash

Git Bash must be installed with specific
configurations, as the discrepancy between
Windows and other operating systems can
cause errors during runtime, if not
properly configured.

To install Git Bash with chocolatey, issue
the following command:

```bash
$ choco install git.install --params "/GitAndUnixToolsOnPath \
        /Editor:Nano /PseudoConsoleSupport /NoAutoCrlf" -y
```

## Install PyCharm, emacs, and Docker

To install necessary development programs
in an easy manner, issue the following
command:

```bash
$ choco install pycharm emacs docker-desktop -y
```

PyCharm is advantageous over other IDEs such
as VSCode because students receive the professional
version of PyCharm for free. Furthermore, PyCharm
offers robust features such as Refactor and Inspect
Code.

A guide to activating PyCharm with a free professional
license is available at <https://youtu.be/QPESX-VBnEU>

## Uninstall anaconda

Development is easier when using a native
Python installation instead of anaconda/conda.

To uninstall anaconda, press the Windows key
and type "Add or remove programs". Then, press
Enter and search for `conda` in the "Search this
list" box. Remove everything related to anaconda.

