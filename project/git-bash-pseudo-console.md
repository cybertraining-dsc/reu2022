# How to Set Up Git Bash with Pseudo Console Support on Windows

If you already have Git Bash installed, then uninstall it
by hitting the Windows key, searching for `Add or remove
programs`, searching for `Git`, clicking on it, then
clicking `Uninstall` and completing the uninstallation wizard.

Then, reinstall (or install for the first time) with chocolatey 
in an instance of Powershell ran as administrator with
`choco install git.install --params "/GitAndUnixToolsOnPath /Editor:Nano /PseudoConsoleSupport" -y`

If you do not have chocolatey then follow the tutorial at
<https://chocolatey.org/install>, or use the standard Git
installer and check the box that reads `Enable experiment 
support for pseudo consoles`.

Now you can use `wsl` and other commands that would otherwise
require `winpty` prepended to the command.

## Troubleshooting

If an `already installed` message appears, such as

```bash
git.install v2.33.0.2 already installed.
 Use --force to reinstall, specify a version to install, or try upgrade.
```

then append `--force` to the end of the `choco install` command.
