# Using Git Bash on Windows

Git Bash is the terminal of choice for the Windows operating
system. However, it must be properly configured for an optimal
Python development experience; for example, Pseudo Console Support
must be enabled.

First, uninstall Git Bash, if already installed.

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
choco command.

For good measure, execute the following in Git Bash to enforce
LF line endings:

```bash
$ git config --global core.autocrlf false
```

Also, generate an ssh-key:

```bash
$ ssh-keygen
# press enter to save to default location
# create a strong memorable password and confirm the password
```

The following is also an ideal `~/.bashrc` file to have for
cloudmesh development on Windows (if you do not have ENV3
Python virtual environment or cm dir, then do
`python -m venv ~/ENV3` and `mkdir ~/cm`). You can create
this `~/.bashrc` file by saying `nano ~/.bashrc` in Git Bash, copying
the text, and then pasting the text with keyboard shortcut
`Shift` + `Insert`. Then say `Ctrl + X`, `y` and `Enter`, and
then `Enter`. An error regarding bash profile after first 
relaunching Git Bash after this created file is expected.

```bash
env=~/.ssh/agent.env

agent_load_env () { test -f "$env" && . "$env" >| /dev/null ; }

agent_start () {
    (umask 077; ssh-agent >| "$env")
    . "$env" >| /dev/null ; }

agent_load_env

# agent_run_state: 0=agent running w/ key; 1=agent w/o key; 2=agent not running
agent_run_state=$(ssh-add -l >| /dev/null 2>&1; echo $?)

if [ ! "$SSH_AUTH_SOCK" ] || [ $agent_run_state = 2 ]; then
    agent_start
    ssh-add
elif [ "$SSH_AUTH_SOCK" ] && [ $agent_run_state = 1 ]; then
    ssh-add
fi

unset env

source ~/ENV3/Scripts/activate
cd ~/cm
```

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
