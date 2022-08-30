# Using Git Bash on Windows

Git Bash is the terminal of choice for the Windows operating
system. However, it must be properly configured for an optimal
Python development experience; for example, Pseudo Console Support
must be enabled.

First, try opening Git Bash and entering `wsl` (you must
have installed WSL and Git Bash). If it hangs, then a reinstall of
Git Bash is necessary. If it does not hang and instead launches into
WSL, then Pseudo Console Support is enabled; however, make sure that
you picked other necessary options when you installed Git Bash.

To enable Pseudo Console Support, uninstall Git Bash.

If you installed Git with `choco`, then do `choco uninstall git`
and `choco uninstall git.install`.

If you did not install Git with `choco` and you instead used
the installer wizard from the Git website, then
press the Windows key, searching for `Add or remove
programs`, searching for `Git`, clicking on it, then
clicking `Uninstall` and completing the uninstallation wizard.

Then install Git Bash in a Run as Administrator instance of Powershell by 
executing the choco command:

```bash
$ choco install git.install --params "/GitAndUnixToolsOnPath \
        /Editor:Nano /PseudoConsoleSupport /NoAutoCrlf" -y
```

If you do not have chocolatey then follow the tutorial at
<https://chocolatey.org/install> and then run the aforementioned
choco command, or forego chocolatey and use the standard Git
installer by checking the box that reads `Enable experiment 
support for pseudo consoles`. Also select the appropriate
options that match what is specified in the previously written
choco command.

Now you can use `wsl` and other commands that would otherwise
require `winpty` prepended to the command.

## Troubleshooting

If an `already installed` message appears when trying to use choco to
install Git Bash, such as

```bash
git.install v2.33.0.2 already installed.
 Use --force to reinstall, specify a version to install, or try upgrade.
```

then try `choco uninstall git`. Then rerun the previously
listed `choco install` command.
If that does not work, consider the `--force` parameter
mentioned in the warning message.
