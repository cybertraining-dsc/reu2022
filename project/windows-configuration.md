# Configuring Windows for REU

Unlike Linux and macOS, Windows runs on a completely different
OS. Most coding environments are adapted to Linux, so Windows users
must properly configure their machine to prepare it for a project.

## Setting Up the Python Environment

As we use Python 3.10.5 from `python.org`, please uninstall Anaconda.
Development is easier when using a native
Python installation instead of anaconda/conda.

To uninstall anaconda, press the Windows key
and type "Add or remove programs". Then, press
Enter and search for `conda` in the "Search this
list" box. Remove everything related to anaconda.

Pycharm and Git Bash can be installed with the instructions found in
*Install.*

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

Uninstall PyCharm Community version if already
installed on the computer by pressing the Windows
key and typing `Add or remove programs` (and
press Enter). Then locate and uninstall PyCharm.

The following command installs PyCharm Professional,
among other necessary development programs.
To install these programs in an easy manner,
issue the following command (you must have 
chocolatey installed):

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

## Preparing for Virtualization

### Docker

To enable virtualization for Docker on Windows machines, some
preparations must be made.  First, if the user has VirtualBox
installed it is suggested that they uninstall it and reinstall later
if necessary. Some older versions of VirtualBox do not support other
virtual images like Windows Subsystem for Linux (WSL).

Next, the BIOS settings must be changed to enable virtualization. To
do this, search `Advanced startup` in the Windows Search Bar and
click `Restart now`. Click `Troubleshoot` and `Advanced startup options`
and then `UEFI` to get into the BIOS. NOTE: These are not exhaustive
instructions because computer brands and hardware differ vastly. The main
objective is to get into the BIOS and search the tabs for any `Virtualization` 
or `Hyper V` options in Windows BIOS configuration. They must be enabled.

Better documentation on enabling virtualization, which is recommended by Docker
and created by Berkeley, is located at <https://bce.berkeley.edu/enabling-virtualization-in-your-pc-bios.html>

Lastly, check Windows features with `Turn Windows features on or off`.
For Docker, `Hyper-V` and `Containers` must be enabled.

### WSL

WSL is a Linux virtual image designed for Windows. WSL 2 is typically
used as opposed to WSL 1. To install, type this into administrative PowerShell:

```shell
wsl --install
```

To install a particular distribution, use `wsl --install -d
<DistroName>` instead. The available distributions can be found with
`wsl --list --online`.

After WSL is installed, it can be accessed by typing `wsl` in
Powershell. More documentation can be found in the [Microsoft 
Official Documentation](https://docs.microsoft.com/en-us/windows/wsl/install).

#### Directories in WSL

WSL creates a Linux environment in your Windows directory. To access
your directories with WSL, a special syntax is used. For example, your
home directory, typically `C:\Users\<USERNAME>` and abbreviated to `~`
is the following with WSL: `/mnt/c/Users/<USERNAME>/`. So to change
directories to the Desktop in WSL, use this command:

```wsl
$ cd /mnt/c/Users/example_user/Desktop
```

`example_user` would be replaced with the name of the User.
