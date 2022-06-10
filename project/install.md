# Install

---

![](images/learning.png) **Learning Objectives**

* Learn how to install python from python.org
* Learn how to use a python venv
* Learn how to install cloudmesh Shell

---

In this section, we present an easy-to-follow installation guide for a 
recent version of python and cloudmesh. 

Before you start, please read the entire section and develop a plan for installation.

## Windows

The installation of cloudmesh benefits from using Git Bash as it allows us to have a terminal that is similar to that of
macOS and Linux.

Hence, before we install python and cloudmesh we install Git Bash.

Furthermore, we provide the option to use chocolatey to install packages in similar fashion as on linus. 

### Git Bash install

To install Git Bash, pleas download it first from 

* <https://git-scm.com/downloads>

Click `Download` for Windows. The download will commence. Please open the file once it is finished downloading. Next,
please start the downloaded program and follow the instructions carefully. 

* The administration window (UAC Prompt) will appear. Click `Yes`. It will show you Git’s  license: a GNU General Public
  License. Read it and Click `Next`. To ensure security of the operating system, a UAC prompt allows operating systems,
  particularly Windows, to prompt for consent or credentials from local administrators before starting a program.
* Click `Next` to confirm that `C:\Program Files\Git` is the directory where you want Git to be installed.
* Select the  box to create a shortcut icon on the desktop. Click `Next`  to continue with the install.
* Click `Next` to accept the default text editor which is vim,
* Replace the default branch name (`master`) with `main`
* Click `Next` again to run Git from the command line and 3rd party software,
* Click `Next` again to use the OpenSSL library
* Click `Next` again to check out Windows-style,
* Click `Next` again to use MinTTY,
* Click `Next` again to use the default git pull,
* Click `Next` again to use the Git Credential Manager Core,
* Click `Next` again to enable file system caching, and then
* Click `Install` because we do not need experimental features.


A video tutorial on how to install Git and Git Bash on Windows 10 is
located at <https://youtu.be/HCotEx_xCfA>

A written tutorial on how to install Git and Git Bash on Windows 10 is located at
<https://cybertraining-dsc.github.io/docs/tutorial/reu/github/git/>


### Python 3.10 install


To install Python 3.10 please go to 

* <https://python.org>

and download the latest version.

* Click `Download`. The download will commence. Please open the file once it is finished downloading

* Click the checkbox `Add Python 3.10 to PATH`

* Click `Install Now`

* At the end of the installation click the option to `Disable path length limit`

A video tutorial on how to install Professional PyCharm is located at
<https://youtu.be/QPESX-VBnEU>

A video on how to configure PyCharm with cloudmesh is located at
<https://youtu.be/eb1IQBx0D50>


### Installing cloudmesh

Cloudmesh can be installed in any shell that has python and `git` access. However, it is convenient to use Git Bash as
it simplifies the documentation and allows us to interact with Linux commands with the Windows file system. The
installation is done with a Python virtual environment `ENV3` using command `venv` so you do not affect your computer's
current python configurations or settings. Here are the steps:

```bash
$ python -m venv ~/ENV3
$ source ~/ENV3/Scripts/activate
$ cd
$ mkdir cm
$ cd cm
$ pip install pip -U
$ pip install cloudmesh-installer 
$ cloudmesh-installer get cmd5 
$ cms help
$ touch .bashrc
$ echo "source ~/ENV3/Scripts/activate" >> .bashrc
$ echo "cd ~/cm" >> .bashrc
```

To activate it, start new Git Bash and terminate the first Git Bash window.  If you see in the new window `(ENV3)`,
continue. Git Bash will initialize the environment.

If you do not want to always start in the directory `cm` do replace the line in your `.bashrc` `cd cm` with `cd`

### Uninstall

To remove the virtual environment `ENV3`, use the following command:

```bash
$ rm -f ~/ENV3
```

Next, edit the `.bashrc` and `.bash_profile` file and delete the lines:

```
$ source ~/ENV3/Scripts/activate
$ cd cm
```

## Choco install 

There are a number of useful packages that you can install via choco. This includes Visual Code, Pycharm, Emacs, and
make. Even Python could be installed with it; however, we have not tested the installation of python via choco, while
we have tested the installation of Emacs, Pycharm, and make.

## Install Chocolatey

To install, pleas start a Git Bash terminal as administrator: To do so press the `Windows` key and type powershell.
Click `Run as Administrator`. Click `Yes`.

2. In PowerShell execute the following command:
   
   ```
   PS C:\Windows\system32> Set-ExecutionPolicy AllSigned
   ``` 
   
   Then type `y`.

3. Next type in the command (copy and paste to not make a mistake)
   
   ```
   PS C:\Windows\system32> Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
   ```

4. Wait for the installation to complete; once you see 
   
  ```
  PS C:\Windows\system32> 
  ``` 
  
   with a blinking cursor again, and lines have stopped appearing,
   then the Chocolatey installation has finished. Type `choco` and you
   should see Chocolatey in green text.

Now you can install many programs with choco by launching PowerShell as Administrator or Git Bash.

A list of programs that you can install with `choco` can be found at:

* <https://community.chocolatey.org/packages/>

## Installing Useful Developer Programs

The following useful developer programs can be installed. Select the once you like and install them with the appropriate command

```bash
$ choco install make -y
$ choco install emacs -y
$ choco install pycharm -y
$ choco install firefox -y
$ choco install vscode -y
$ choco install zoom -y
``` 

Once the installation completes, your program will be ready for you to use.

## Linux 

### Install Python 3.10.5

The installation from source can be done easily as shown:

```bash
$ mkdir -p ~/tmp
$ cd ~/tmp
$ wget https://www.python.org/ftp/python/3.10.5/Python-3.10.5.tar.xz
$ tar xvf Python-3.10.5.tar.xz 
$ cd Python-3.10.5/
$ ./configure --enable-optimizations
$ make -j $(nproc)
$ sudo make altinstall
$ pip install pip -U
$ python3.10 -V
```

### Setting up the venv

We assume you use bash

```bash
$ python3.10 -m venv ~/ENV3
$ source ~/ENV/bin/activate
$ cd
$ mkdir cm
$ cd cm
$ pip install cloudmesh-installer 
$ cloudmesh-installer get cmd5 
$ cms help
$ touch .bashrc
$ echo "source ~/ENV3/bin/activate" >> .bashrc
$ echo "cd cm" >> .bashrc
$ echo "source ~/ENV3/bin/activate" >> .bash_profile
$ echo "cd cm" >> .bash_profile
```

### Uninstall

```bash
$ rm -f ~/ENV3
```

Edit the `.zshrc` and `.zprofile` file and delete the lines

```
$ source ~/ENV3/bin/activate
$ cd cm
```

### Update

In case you need to update the Python version it is sufficient to
follow the instructions provided in the section `Install Python
3.10.5`, while replacing the version number with the current python
release number.

In case you need to create a new virtual ENV3. You can first uninstall
it and then reinstall it.

An easy way to do all of this with a command is the following:

```bash
$ cd ~/cm
$ pip install cloudmesh-installer -U
$ pip install --upgrade pip
$ cloudmesh-installer new ~/ENV3 cmd5 --python=/usr/local/bin/python3.10
$ source ~/ENV3/bin/activate
$ python -V
$ which python
```


## macOS

We assume you use `~/zsh` which is the default on macOS

### Xcode Install

There are a number of digital tools that are needed before proceeding further. These
tools include git, make, and a c compiler. All of these tools can be downloaded at
[Xcode](https://apps.apple.com/us/app/xcode/id497799835), which is an IDE App on the 
Apple App Store that includes all of these necessary elements. 

Once installed, there is one simple command line command to run:

```bash
$ xcode-select --install
```

This will install all the necessary command line tools. Xcode can be used as an IDE, but for
the most part will not be used outside the command line tools it provides. 

### Cloudmesh

#### Install

Before any of the following, make sure to download the current version
of python. At the time of this writing, it is python 3.10.5.

Second, execute the following commands in your terminal. Make sure to
do this in order.

```bash
$ cd
$ python3.10 -m venv ~/ENV3
$ source ~/ENV/bin/activate
$ pip install pip -U
$ mkdir cm
$ cd cm
$ pip install cloudmesh-installer 
$ cloudmesh-installer get cmd5 
$ cms help
$ echo "source ~/ENV3/bin/activate" >> .zshrc
$ echo "cd cm" >> .zshrc
$ echo "source ~/ENV3/bin/activate" >> .zprofile
$ echo "cd cm" >> .zprofile
```

It creates the virtual environment, a directory called `~/cm`, then installs `cloudmesh`. Following this, it sets the
macOS startup commands `.zshrc` and `.zprofile` to start up in the virtual environment `~/ENV3`.

#### Uninstall

```bash
$ rm -rf ~/ENV3
````

You may need to enter your system password. 

### Updating Python

Before starting this process, ensure that python is in the correct path. Test in the terminal. 

To do so remove the existing ENV3 first and start a new terminal in which you will be working.

```bash
$ rm -rf ~/ENV3
```

Start the new terminal and execute the commands to verify if you have the right updated version of python

```bash
$ which python3.10
$ where python3.10
$ python3.10 -V
```

Now execute:

```bash
$ cd ~/cm
$ python3.10 -m venv ~/ENV3
$ source ~/ENV3/bin/activate
$ pip install pip -U
$ pip install cloudmesh-installer 
$ cloudmesh-installer get cmd5 
$ cms help
```

As `~/zsh` is already configured previously, we do not have to set it up again.

### Homebrew install 

Homebrew is a package management software. The Homebrew command is called `brew`. It is used to install Linux packages
on macOS. Installing `brew` is simple. 

* First, make sure the computer that is downloading Homebrew is 
  up-to-date with the latest software for its OS. 

* Second, ensure that `xcode` has been installed. `xcode` can be installed from the Apple App Store.

* Third, in the terminal, write out: 

  ```bash
  $ xcode-select --install
  ```

  This installs `xcode` command line tools. 

* Fourth, run the following command in the terminal:

  ```bash
  $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  ```

* Fifth, enter the administrator password into the desired location. 

* It may take a moment for the software to install, but it will
  eventually say **"Installation successful!"** in the terminal. After
  that, Homebrew is installed onto the device.

After the user has correctly installed Homebrew, it is simple to
install packages directly to the operating system:

```bash
$ brew install [package name]
```