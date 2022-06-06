# Install

TODO: Abdul


Improve the instalation instructions for python in the book.

## Windows

Install gitbash from <https://git-scm.com/downloads>

TODO: document the options


Install python from <https://python.org>

Document the options, e.g. switch on path, icon on deskto, allow path longer then 256 chars

Start gitbash

TODO fix as appropriate and document here

```bash
cd
python3.10 -m venv ~/ENV3
source ~/ENV/Scripts/activate
mkdir cm
cd cm
pip install cloudmesh-installer 
cloudmesh-installer get cmd5 
cms help
touch .bashrc
echo "cd cm" >> .bashrc
echo "source ~/ENV3/Scripts/activate" >> .bashrc
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



