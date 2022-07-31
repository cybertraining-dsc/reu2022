# Using Git Bash on Windows

If you do not use wsl, you can skip the appropriate steps related to it.

First, try opening Git Bash and entering `wsl` (you must
have installed wsl). If it hangs, then follow the rest of this
tutorial. If it does not hang, you do not need to follow this
tutorial since you already have Pseudo Console Support.

If you already have Git Bash installed, then uninstall it one
of several ways.

If you installed Git with `choco`, then do `choco uninstall git`
and `choco uninstall git.install`.

If you did not install Git with `choco` and you instead used
the installer wizard from the Git website, then
press the Windows key, searching for `Add or remove
programs`, searching for `Git`, clicking on it, then
clicking `Uninstall` and completing the uninstallation wizard.

Then, reinstall (or install for the first time) with chocolatey 
in an instance of Powershell ran as administrator with

```bash
$ choco install git.install --params "/GitAndUnixToolsOnPath \
        /Editor:Nano /PseudoConsoleSupport /NoAutoCrlf" -y
```

If you do not have chocolatey then follow the tutorial at
<https://chocolatey.org/install> and then run the aforementioned
choco command, or forego chocolatey and use the standard Git
installer by checking the box that reads `Enable experiment 
support for pseudo consoles`.

Now you can use `wsl` and other commands that would otherwise
require `winpty` prepended to the command.

## Troubleshooting

If an `already installed` message appears, such as

```bash
git.install v2.33.0.2 already installed.
 Use --force to reinstall, specify a version to install, or try upgrade.
```

then try `choco uninstall git`. Then rerun the previously
listed `choco install` command.
If that does not work, consider the `--force` parameter
mentioned in the warning message.
