# Install

TODO: Abdul


Improve the instalation instructions for python in the book.

## Windows

Install gitbash from <https://git-scm.com/downloads>

A video tutorial on how to install Git and Git Bash on Windows 10 is located at <https://youtu.be/HCotEx_xCfA>

A written tutorial on how to install Git and Git Bash on Windows 10 is located at <https://cybertraining-dsc.github.io/docs/tutorial/reu/github/git/>

A video tutorial on how to install Professional PyCharm is located at <https://youtu.be/QPESX-VBnEU>

TODO: document the options


Install python from <https://python.org>

Document the options, e.g. switch on path, icon on deskto, allow path longer then 256 chars

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
echo "cd cm" >> .bashrc
echo "source ~/ENV3/Scripts/activate" >> .bashrc
echo "cd cm" >> .zprofile
echo "source ~/ENV3/Scripts/activate" >> .zrofile
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
echo "cd cm" >> .zshrc
echo "source ~/ENV3/Scripts/activate" >> .zshrc
echo "cd cm" >> .zprofile
echo "source ~/ENV3/Scripts/activate" >> .zprofile
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
...
```
even python could be installed with it however we have not tested, if it adds python to the path or sets the maxmunm oath to greated then 256. For that reason we recommend to install python the regular way as documented in the video ... jps video


