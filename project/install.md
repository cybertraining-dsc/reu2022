# Install

In this section, we present an easy to follw instalation for a 
recent version of python and cloudmesh. 

Before you start doing the install, please read the entire section and develop a plan for installation.

## Windows

The instalation of cloudmesh benefits from using gitbash as it allows us to have a terminal that is similar to that of macOS and Linux.

Hence before we install python and cloudmesh we install gitbash.

Furthermore, we provide the option to use chocolatey to install packages in similar fashion as on linus. 

### Git Bash install

To install gitbash, pleas download it forst from 

* <https://git-scm.com/downloads>

Click `Download` for Windows. The download will commence. Please
open the file once it is finished downloading.
 
Next you start the downloaded program and follw the install screens carfully. 

TODO: what is a UAC?


* The UAC Prompt will appear. Click `Yes`. It will show you Git’s  license: a GNU General Public License. Read it and Click `Next`.
  To ensure security of the operating system a UAC prompt allows 
  operating systems, particularly windows, to prompt for consent
  or credentials from local administrators before starting a 
  program.
* Click `Next` to confirm that `C:\Program Files\Git` is the directory
  where you want Git to be installed.

* Select the  box to create a shortcut icon on the desktop. 
  Click `Next`  to continue with the install.

* Click `Next` to accept the default text editor which is vim, 
* TODO: THIS IS WRONG, you do want the one with main 
  Click `Next` again to Let Git decide the default branch name
* Click `Next` again to run Git from the command line and 3rd party software,
* Click `Next` again to use the OpenSSL library
* Click `Next` again to checkout Windows-style,
* Click `Next` again to use MinTTY,
* Click `Next` again to use the default git pull,
* Click `Next` again to use the Git Credential Manager Core,
* Click `Next` again to enable file system caching, and then
* Click `Install` because we do not need experimental features.

TODO: the 256 path length is missing which will be done at the end.

A video tutorial on how to install Git and Git Bash on Windows 10 is
located at <https://youtu.be/HCotEx_xCfA>

A written tutorial on how to install Git and Git Bash on Windows 10 is located at
<https://cybertraining-dsc.github.io/docs/tutorial/reu/github/git/>


### Python 3.10 install


To install python 3.10 please go to 

* <https://python.org>

and download the latest version.

* Click `Download`. The download will commence. Please open the file
  once it is finished downloading

* Click `Add python 3.10 to path`

* Click `Install now`

TODO: veriify if the pathlength option appears here or in gitbash or both.

A video tutorial on how to install Professional PyCharm is located at
<https://youtu.be/QPESX-VBnEU>

A video on how to configure PyCharm with cloudmesh is located at
<https://youtu.be/eb1IQBx0D50>


### Installing cloudmesh

Cloudmesh can be installed in any shell that has python and git access. HOwever it is convenient t use gitbash as it simplifies the documentation and allows us to interact with linux commands with the windows file system. The installation is done with a Pyython `venv` so you do not effect your computres python install. Here are the steps:

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

To activate it, start new gitbash and terminate the first gitbash window.  If you see in the new window
`(ENV3)`, continue. Git bash will initialize the environment.
It will set now up some envireonment and thus you will start 
again gitbash and terminate the second gitbash you created. Now
gitbash is properly created and configures.

If you do not want to always start in the directory `cm` do replace
the line in your `.bashrc` `cd cm` with `cd`

### Uninstall

```bash
$ rm -f ~/ENV3
```

Edit the .bashrc and .bash_profile file and delete the lines

```
$ source ~/ENV3/Scripts/activate
$ cd cm
```

## Choco install 

There are a number of usefull packages that you can install via choco
this includes visual code, pychram, emacs, and make

Even python could be installed with it however we have not tested the install of python via choco. However we tested the install of emacs, pychram, and make.

## Install Chocolatey

To install pycharm, pleas esatrt a gitbash terminal as administrator: To do so press the `Windows` key and type powershell. Click Run as Administrator. Click Yes.

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

Once teh install completes PyCharm will be ready for you to use. You
can install many programs this way, and the


## Linux 

### Install Python 3.10.5

The instalatiton form source can be done easily as shown next

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

It creates the virtual environment, a directory called `cm`, then installs
`cloudmesh`. Following this, it sets the macOS startup commands
`.zshrc` and `.zprofile` to start up in the virtual environment
`ENV3`.

#### Uninstall

```bash
$ rm -rf ~/ENV3
````

You may need to enter your system password. 

### Updating Python

Before starting this process, ensure that python is in the correct
path. Test in the terminal. 

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

Now execute

```bash
$ cd ~/cm
$ python3.10 -m venv ~/ENV3
$ source ~/ENV3/bin/activate
$ pip install cloudmesh-installer 
$ cloudmesh-installer get cmd5 
$ cms help
```

As `zsh` is already configured previously, we do not have to set it up again.

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




