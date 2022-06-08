# Install

TODO: Abdul

Improve the installation instructions for python in the book.

## Windows

### Git Bash install

* Install gitbash from <https://git-scm.com/downloads>
 
* Click `Download` for Windows. The download will commence. Please
  open the file once it is finished downloading.

* The UAC Prompt will appear. Click `Yes` because Git is a safe
  program. It will show you Git’s license: a GNU General Public
  License. Click `Next`.

* Click `Next` to confirm that `C:\Program Files\Git` is the directory
  where you want Git to be installed.

* Click `Next` unless you would like an icon for Git on the desktop
  (in which case you can check the box and then click `Next`).

* Click `Next` to accept the text editor,
* Click `Next` again to Let Git decide the default branch name
* Click `Next` again to run Git from the command line and 3rd party software,
* Click `Next` again to use the OpenSSL library
* Click `Next` again to checkout Windows-style,
* Click `Next` again to use MinTTY,
* Click `Next` again to use the default git pull,
* Click `Next` again to use the Git Credential Manager Core,
* Click `Next` again to enable file system caching, and then
* Click `Install` because we do not need experimental features.

A video tutorial on how to install Git and Git Bash on Windows 10 is
located at <https://youtu.be/HCotEx_xCfA>

A written tutorial on how to install Git and Git Bash on Windows 10 is
located at
<https://cybertraining-dsc.github.io/docs/tutorial/reu/github/git/>


### Python 3.10 install

* Install python from <https://python.org>

* Click `Download`. The download will commence. Please open the file
  once it is finished downloading

* Click `Add python 3.10 to path`

* Click `Install now`

A video tutorial on how to install Professional PyCharm is located at
<https://youtu.be/QPESX-VBnEU>

A video on how to configure PyCharm with cloudmesh is located at
<https://youtu.be/eb1IQBx0D50>

Document the options, e.g. switch on path, icon on desktop, allow path
longer then 256 chars

Start gitbash

```bash
$ python -m venv ~/ENV3
$ source ~/ENV3/Scripts/activate
$ cd
# mkdir cm
$ cd cm
$ pip install pip -U
$ pip install cloudmesh-installer 
$ cloudmesh-installer get cmd5 
$ cms help
$ touch .bashrc
$ echo "source ~/ENV3/Scripts/activate" >> .bashrc
$ echo "cd ~/cm" >> .bashrc
```

start new gitbash and remove the first gitbash window, see if you see
(ENV3) and continue. Git bash will initialize the environment

start now again gitbash and remove the second gitbash you created. Now
gitbash is properly created.

If you do not want to always start in the directory `cm` do replace
the line in your `.bashrc` `cd cm` with `cd`

### Uninstall

```bash
$ rm -f ~/ENV3
```

Edit the .zshrc and .zprofile file and delete the lines

```
$ source ~/ENV3/Scripts/activate
$ cd cm
```

## Choco install 

There are a number of usefull packages that you can install via choco
this includes visual code, pychram, emacs, and make

```bash
$ choco install make
$ choco install emacs
$ choco install pycharm
$ choco install firefox
$ choco install vscode
$ choco install zoom
```

Even python could be installed with it however we have not tested, if
it adds python to the path or sets the maxmunm oath to greated then
256. For that reason we recommend to install python the regular way as
documented in the video ... jps video

## Choco install pycharm

* Press the Windows key and type powershell. Click Run as Administrator. Click Yes.

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

Now you can install many programs by launching PowerShell as
Administrator or gitbash.

A list of programs that you can install with `choco` can be found at

* <https://community.chocolatey.org/packages/>

## Installing Pycharm

PyCharm can be installed in gitbash with choco while typing 

```
$ choco install pycharm -y
``` 

Once teh install completes PyCharm will be ready for you to use. You
can install many programs this way, and the


## Linux 

### Install Python 3.10.5

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

### Setting up the a venv

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

Edit the .zshrc and .zprofile file and delete the lines

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
$ cloudmesh-installer new ~/ENV3 cmd5 --python=/usr/local/bin/python3.10
$ source ~/ENV3/bin/activate
$ python -V
$ which python
```


## macOS

We assume you use zsh which is the default on macOS

### Cloudmesh

#### Install

Before any of the following, make sure to download the current version
of python. At the time of this writing, it is python 3.10.5

Second, execute the following commands in your terminal. Make sure to
do this in order.

```bash
$ cd
$ python3.10 -m venv ~/ENV3
$ source ~/ENV/bin/activate
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

In a short summary, this essentially creates the virtual environment,
creates another directory called `cm`, then installs
`cloudmesh`. Following this, it sets the macOS startup commands
`.zshrc` and `.zprofile` to start up in the virtual environment
`ENV3`.

#### Uninstall

```bash
$ rm -f ~/ENV3
```

### Updating Python

Before starting this process, ensure that python is in the correct
path.  This can be checked by following the scripting below:

```bash
$ which python # should print user/ENV3/bin/python

$ python3.10 --version # should print the current version of python in the venv
```
Then, follow the directions below: 

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
  
Essentially, what this does is it updates everything within the virtual environment that
you have set up and retains the py cache that has already been established in the 
environment. 

`venv` comes with a built-in function called `--upgrade`. This will upgrade everything in 
the virtual environment, but it will not retain the py cache that has been established. Thus,
it is necessary to follow the first set of commands. 

### Homebrew install 

Homebrew (`brew`) like `choco` is a package management
software. Unlike choco`, it is used by macOS devices rather than
Windows devices.  `brew` is used to more easily download packages to
an operating system; simply put, it eliminates the need for the user
to search for and download the desired package.

Installing `brew` is simple. 

* First, make sure the computer that is downloading Homebrew is 
  up-to-date with the latest software for its OS. 

* Second, ensure that `xcode` has been installed. `xcode`
  can be installed from the Apple App Store.

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




