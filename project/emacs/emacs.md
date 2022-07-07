# emacs

emacs is a command line editor that can be used to write
bash scripts which are then used for specific purposes.

In the REU program, we used emacs to create changes in the `.zshrc` and `.zprofile` (for mac/linux) and the `.bashrc` and `.bashprofile` (for Windows). 

## Downloading and Installing

In order to download and install emacs, there are two paths that one can take. 

For Mac:

* Go to [Aquamacs](https://aquamacs.org/), which is a website that allows Mac users to download and install emacs. 
* After that, follow the GUI installation instructions and then you should be able to launch the application from the command line or from the GUI dashboard. 

## Editing `.zprofile` and `.zshrc` for the REU

The `.zprofile` and `.zshrc` bash scripts are scripts that are run upon starting up a terminal for mac (the command line). In order to set up this for the correct usage, we will be editing these scripts to contain the correct virtual environment so that we can correctly use it. 

`.zprofile`

```bash
# Setting PATH for Python 3.9
# The original version is saved in .zprofile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/3.9/bin:${PATH}"
export PATH

# Setting PATH for Python 3.10
# The original version is saved in .zprofile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/3.10/bin:${PATH}"
export PATH

PATH="~/ENV3/bin:${PATH}"
export PATH

source ~/ENV3/bin/activate
```

`.zshrc`

```bash
PATH="~/ENV3/bin:${PATH}"
export PATH

source ~/ENV3/bin/activate
```

In essence, this is sets up the `.zshrc` and `.zprofile` scripts to have the correct virtual environment. 

If you have a different OS, Aquamacs also has other versions to support those OSes, but you could also use vi or another text editor.