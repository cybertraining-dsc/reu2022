# Configuring Windows for REU

Unlike Linux and MacOS, Windows runs on a completely different
OS. Most coding environments are adapted to Linux, so Windows users
must properly configure their machine to prepare it for a project.

## Setting Up the Python Environment

As we use Python 3.10.5 from `python.org`, please uninstall Anaconda.
This can be done with `Add or remove programs`.

Pycharm and Git Bash can be installed with the instructions found in
*Install.*

## Preparing for Virtualization

### Docker

To enable virtualization for Docker on Windows machines, some
preparations must be made.  First, if the user has VirtualBox
installed it is suggested that they uninstall it and reinstall later
if necessary. Some older versions of VirtualBox do not support other
virtual images like Windows Subsystem for Linux (WSL).

Next, the BIOS settings must be changed to enable virtualization. To
do this, search up `Advanced starup` in the Windows Search Bar and
restart your computer.  Next, find the `Virtualization` option in
Windows BIOS configuration. This must be enabled.

Lastly, check Windows features with `Turn Windows features on or off`.
For Docker, `Hyper-V` and `Containers` must be enabled.

### WSL

WSL is a Linux virtual image designed for Windows. WSL 2 is typically
used as opposed to WSL 1. To install, type this into Powershell:

```shell
wsl --install
```

To install a particular distribution, use `wsl --install -d
<DistroName>` instead. The available distributions can be found with
`wsl --list --online`.

After WSL is installed, it can be accessed by typing `wsl` in
Powershell. More documentation can be found in the [Microsoft 
Official Documentation](<https://docs.microsoft.com/en-us/windows/wsl/install>).

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