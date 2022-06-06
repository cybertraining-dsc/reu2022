# Install

TODO: Abdul


Improve the instalation instructions for python in the book.

## Windows


### Git Bash install

* Open a web browser and search``` git```. Look for the result that is from ```git-scm.com``` and click Downloads.
* Click ```Download``` for Windows. The download will commence. Please open the file once it is finished downloading.

* The UAC Prompt will appear. Click ```Yes``` because Git is a safe program. It will show you Git’s license: a GNU General Public License. Click ```Next```.

* Click``` Next``` to confirm that ```C:\Program Files\Git``` is the directory where you want Git to be installed.

* Click ```Next``` unless you would like an icon for Git on the desktop (in which case you can check the box and then click ```Next```).

* Click``` Next``` to accept the text editor,
* Click ```Next``` again to Let Git decide the default branch name
* Click ```Next``` again to run Git from the command line and 3rd party software,
* Click ```Next``` again to use the OpenSSL library
* Click ```Next``` again to checkout Windows-style,
* Click ```Next``` again to use MinTTY,
* Click ```Next``` again to use the default git pull,
* Click ```Next``` again to use the Git Credential Manager Core,
* Click ```Next``` again to enable file system caching, and then
* Click ```Install``` because we do not need experimental features.

Install gitbash from <https://git-scm.com/downloads>

A video tutorial on how to install Git and Git Bash on Windows 10 is located at <https://youtu.be/HCotEx_xCfA>

A written tutorial on how to install Git and Git Bash on Windows 10 is located at <https://cybertraining-dsc.github.io/docs/tutorial/reu/github/git/>

A video tutorial on how to install Professional PyCharm is located at <https://youtu.be/QPESX-VBnEU>

### python 3.10 install
* Install python from <https://python.org>

Document the options, e.g. switch on path, icon on desktop, allow path longer then 256 chars

Start gitbash

TODO fix as appropriate and document here

```bash
python -m venv ~/ENV3
source ~/ENV3/Scripts/activate
cd
mkdir cm
cd cm
pip install pip -U
pip install cloudmesh-installer 
cloudmesh-installer get cmd5 
cms help
touch .bashrc
echo "source ~/ENV3/Scripts/activate" >> .bashrc
echo "cd ~/cm" >> .bashrc
```

start new gitbash and remove the first gitbash window, see if you see (ENV3) and continue. Git bash will initialize the environment

start now again gitbash and remove the second gitbash you created. Now gitbash is properly created.

If you do not want to always start in the directory `cm` do replace the line in your `.bashrc`
`cd cm` with `cd`

### Uninstall

```bash
rm -f ~/ENV3
```

Edit the .zshrc and .zprofile file and delete the lines

```
source ~/ENV3/Scripts/activate
cd cm
```


## Linux 

We assume you use bash

```bash
cd
python3.10 -m venv ~/ENV3
source ~/ENV/bin/activate
mkdir cm
cd cm
pip install cloudmesh-installer 
cloudmesh-installer get cmd5 
cms help
touch .bashrc
echo "source ~/ENV3/bin/activate" >> .bashrc
echo "cd cm" >> .bashrc
echo "source ~/ENV3/bin/activate" >> .zrofile
echo "cd cm" >> .zprofile
```

### Uninstall

```bash
rm -f ~/ENV3
```

Edit the .zshrc and .zprofile file and delete the lines

```
source ~/ENV3/bin/activate
cd cm
```

## macOS

We assume you use zsh which is the default on macOS

```bash
cd
python3.10 -m venv ~/ENV3
source ~/ENV/bin/activate
mkdir cm
cd cm
pip install cloudmesh-installer 
cloudmesh-installer get cmd5 
cms help
echo "source ~/ENV3/bin/activate" >> .zshrc
echo "cd cm" >> .zshrc
echo "source ~/ENV3/bin/activate" >> .zprofile
echo "cd cm" >> .zprofile
echo "source ~/ENV3/Scripts/activate" >> .zprofile
```


### Uninstall

```bash
rm -f ~/ENV3
```

Edit the .zshrc and .zprofile file and delete the lines

```
source ~/ENV3/bin/activate
cd cm
```


## Choco install 

There are a number of usefull packages that you can install via choco this includes visual code, pychram, emacs, and make
```bash
choco install make
choco install emacs
choco install pycharm
choco install firefox
choco install vscode
choco install zoom
```

even python could be installed with it however we have not tested, if it adds python to the path or sets the maxmunm oath to greated then 256. For that reason we recommend to install python the regular way as documented in the video ... jps video

## Choco install pycharm

1. Press the Windows key and type powershell. Click Run as Administrator. Click Yes.

2. Copy this:```Set-ExecutionPolicy AllSigned``` and then go to PowerShell (the blue window) and paste it in. Press Enter. Then type ``` y ``` and press Enter.

3. Copy this: ``` Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))``` and then go back to PowerShell, paste it in, and press Enter.

5. Wait for the installation to complete; once you see ``` PS C:\Windows\system32> ``` with a blinking cursor again, and lines have stopped appearing, then the Chocolatey installation has finished. Type ``` choco ```and press Enter and you should see Chocolatey in green text. Congratulations! Now you can install many programs by launching PowerShell as Administrator. Let's install pycharm.

6. Type ``` choco install pycharm ``` and press Enter. When it asks if you want to run the script, type ```a``` and press Enter. You can watch the install process, and once complete, Visual Studio Code will be ready for you to use. You can install many programs this way, and the total list of programs can be found here: <https://community.chocolatey.org/packages/>

## Homebrew install 

Homebrew (a.k.a. ```brew```) like ```choco``` is a package management software. Unlike
```choco```, it is used by macOS devices rather than Windows devices.
```brew``` is used to more easily download packages to an operating
system; simply put, it eliminates the need for the user to search for
and download the desired package. 

Installing ```brew``` is simple. 

* First, make sure the computer that is downloading Homebrew is 
up-to-date with the latest software for its OS. 

* Second, ensure that ```xcode``` has been installed. ```xcode```
can be installed from the Apple App Store.

* Third, in the terminal, write out: 

```bash
xcode-select --install
```

This installs ```xcode``` command line tools. 

* Fourth, run the following command in the terminal:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

* Fifth, enter the administrator password into the desired location. 

* It may take a moment for the software to install, but it will 
eventually say **"Installation successful!"** in the terminal. After that,
Homebrew is installed onto the device. 

After the user has correctly installed Homebrew, it is simple to 
install packages directly to the operating system:

```bash
brew install [package name]
```

Most of this documentation was found at the following link:

[Phoenix Nap](https://phoenixnap.com/kb/install-homebrew-on-mac)



