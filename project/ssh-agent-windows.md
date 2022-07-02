# How to Auto-launch SSH Agent on Windows

Copy the following code:

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

alias emacs="C:/ProgramData/chocolatey/bin/emacs.exe"
alias tree="cmd //c tree.com //a //f"
source ~/ENV3/Scripts/activate
cd ~/cm
```

Then, using Git Bash, run `nano ~/.bashrc`, use the down arrow key to ensure you
are at the bottom of the file on a new line, and then paste the contents using
`Shift + Insert`. Consider, beforehand, even deleting the `.bashrc` if you have a 
preexisting script that may conflict with the new additions and then creating a
new `.bashrc` with the above contents.

Keep in mind that if emacs is not installed using choco, the emacs alias will not
function. You can install emacs using choco by running `choco install emacs`. This
will not work if you have not installed choco.

Additionally, the source command will not work if you have not created a virtual
Python environment named `ENV3` in your home dir.

The `cd` will also not function if `cm` dir does not exist in the home dir.
If so, then execute `mkdir ~/cm`.

