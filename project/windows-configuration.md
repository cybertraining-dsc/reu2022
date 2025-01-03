# Configuring Windows for Research

Unlike Linux and macOS, Windows runs on a completely different
OS. Many coding environments are adapted to Linux, so Windows users
must properly configure their machine to prepare it for a project.
This is of special importance when working in environments supporting 
distributed cyberinfrastructure. Here in many cases Linux is required.

## Setting Up the Python Environment

Often you need a specific version of Python. If in doubt, please 
install the newest one. At time of writing this document it 
is Python 3.10.5.

Please download and install it from  `python.org`.
We recommend that you uninstall Anaconda if you used that before 
and use the verison from python.org instead..
Development is easier when using a native
Python installation instead of anaconda/conda.

To uninstall anaconda, press the Windows key
and type "Add or remove programs". Then, press
Enter and search for `conda` in the "Search this
list" box. Remove everything related to anaconda. 
Note that anaconda may have set some environment 
variables or added configuration scripts to your `.bashrc`
files in case you use gitbash. Please, remove them and make sure your 
Python version from python.org works as expected.

To code in Python, we recommend using PyCharm and not VSCode.

Pycharm and Git Bash can be installed with the instructions found in
*Install.*

Installation may be simplified while using chocolatey.

This includes

* gitbash
* pycharm
* emacs
* docker

Before installing docker however you have to set up the 
appropriate hypervisor at boot time. PLease let us know how 
you set them for your machine, so we can add some information here. 
You will likely have to research it.

Please also know that you MUST uninstall virtualbox before you 
install docker, as old versions of virtualbox are incompatible 
with docker and it is just easier to uninstall virtualbox and reinstall it.

Next we summarize the installations using chocolatey.

Before installing anything, we recommend that you read the entire section. 
Especially when installing docker and if you do not have a brand new computer.

## Install Chocolatey

To install chocolatey, follow the tutorial
at <https://github.com/cybertraining-dsc/cybertraining-dsc.github.io/blob/main/content/en/docs/tutorial/reu/chocolatey/index.md>

## Install Git Bash

Git Bash must be installed with specific
configurations, as the discrepancy between
Windows and other operating systems can
cause errors during runtime, if not
properly configured. If Git Bash is already
installed, uninstall it by pressing the Windows
key and typing `Add or remove programs` (and
press Enter). Then locate and uninstall Git Bash.

To install Git Bash with chocolatey, issue
the following command:

```bash
choco install openssh git.install --params "'/GitAndUnixToolsOnPath /Editor:Nano /PseudoConsoleSupport /NoAutoCrlf /NoOpenSSH'" -y
```

The `/NoAutoCrlf` sets it so that the files are
not downloaded via git with Windows line endings.
If it were downloaded with such line endings, then
it would cause programming bugs. Programmers should
Commit As-Is to avoid conflicts.

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

## Configure PyCharm

### Set hard wrap

Press `Ctrl + Alt + S` in PyCharm and expand the
`Editor` menu on the left-hand side. Then, click
on `Code Style` and enter `79` in the `Hard wrap at:`
box. Also, check the `Wrap on typing` checkbox.

This is done so that the text in files is uniformly
indented at 79 columns.

### Makefile Tab configuration and formatting

To change what the Tab key does in a Makefile,
open a Makefile in PyCharm and click on `Tab`
in the bottom right of the PyCharm interface.
If you cannot find the `Tab` button, then click
on `View` in the top-right, go to `Appearance`,
and make sure `Status Bar` is checked.

After clicking the `Tab` button in the
bottom-right, click on `Configure Indents for
Makefile...` Tab size should be 4.

If PyCharm fails to render your Makefile correctly,
right-click on the Makefile in your open files tabs
and click `Override File Type`. If you cannot find
`Makefile` in the list, you must install the `Makefile
Language plugin` for PyCharm.

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
and then `UEFI Firmware Settings` to get into the BIOS. NOTE: These are 
not exhaustive instructions because computer brands and hardware differ 
vastly. The main objective is to get into the BIOS and search
for any `Virtualization` or `Hyper V` options in Windows BIOS configuration.
For example, Lenovo brand laptops have a `Configure` tab in the BIOS
and the virtualization settings must be enabled under that menu.
Then, the user must exit the BIOS while saving changes.

Better documentation on enabling virtualization, which is recommended by Docker
and created by Berkeley, is located at <https://bce.berkeley.edu/enabling-virtualization-in-your-pc-bios.html>

Lastly, check Windows features with `Turn Windows features on or off`.
For Docker, `Hyper-V` and `Containers` must be enabled.

### WSL

WSL is a Linux virtual image designed for Windows. WSL 2 is typically
used as opposed to WSL 1. To install, type this into administrative PowerShell:

```shell
PS> wsl --install
```

To install a particular distribution, use `wsl --install -d
<DistroName>` instead. The available distributions can be found with

```
PS> wsl --list --online
```

After WSL is installed, it can be accessed by typing `wsl` in
Powershell. More documentation can be found in the [Microsoft 
Official Documentation](https://docs.microsoft.com/en-us/windows/wsl/install).

#### Directories in WSL

WSL creates a Linux environment in your Windows directory. To access
your directories with WSL, a special syntax is used. For example, your
home directory, typically `C:\Users\USERNAME` and abbreviated to `~`
is the following with WSL: `/mnt/c/Users/USERNAME/`. So to change
directories to the Desktop in WSL, use this command:

```wsl
$ cd /mnt/c/Users/USERNAME/Desktop
```

where `USERNAME` is to be replaced with the name of the user.

## bashrc

```bash
# Path to the SSH agent environment file
SSH_ENV="$HOME/.ssh/agent.env"

# Function to load existing SSH agent environment
agent_load_env() {
    test -f "$SSH_ENV" && . "$SSH_ENV" >| /dev/null
}

# Function to check if the SSH agent is running
agent_running() {
    [ -n "$SSH_AGENT_PID" ] && ps -p $SSH_AGENT_PID > /dev/null 2>&1
}

# Function to start a new SSH agent
agent_start() {
    echo "Starting a new SSH agent..."
    (umask 077; ssh-agent >| "$SSH_ENV")
    . "$SSH_ENV" >| /dev/null
}

# Load existing SSH agent environment or start a new one if necessary
agent_load_env
if ! agent_running; then
    agent_start
fi

# Add SSH key only if no identities are loaded
if ! ssh-add -l > /dev/null 2>&1; then
    ssh-add ~/.ssh/id_rsa
fi


# -----------------------------------
# Emulate ssh-copy-id in Git Bash
# -----------------------------------
ssh-copy-id() {
    local userhost="$1"

    if [ -z "$userhost" ]; then
        echo "Usage: ssh_copy_id user@host"
        return 1
    fi

    # Check which public key exists in ~/.ssh
    local pubkey
    if [ -f "$HOME/.ssh/id_ed25519.pub" ]; then
        pubkey="$HOME/.ssh/id_ed25519.pub"
    elif [ -f "$HOME/.ssh/id_rsa.pub" ]; then
        pubkey="$HOME/.ssh/id_rsa.pub"
    else
        echo "No valid public key found in ~/.ssh. Generate one with ssh-keygen first."
        return 1
    fi

    echo "Using public key: $pubkey"
    echo "Copying key to $userhost..."

    # Copy the key to the remote host’s authorized_keys
    cat "$pubkey" | ssh "$userhost" "mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"
    
    echo "Key copied. You should now be able to SSH into $userhost without a password (assuming your SSH agent is running)."
}

source ~/ENV3/Scripts/activate
cd ~/cm
```

