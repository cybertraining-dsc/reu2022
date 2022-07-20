# How to Install WSL Ubuntu 22.04 on Command Line for Windows

We assume that you have installed gitbash with support for pseudo console. If not or you are not sure, we recommend that you reinstall Git Bash with this tutorial: <https://github.com/cybertraining-dsc/reu2022/blob/main/project/git-bash-pseudo-console.md> We also need you to enable Linux line ending support through "NoAutoCrlf" (which is included in the previously linked tutorial) as some of our cloudmesh programs when interacting with wsl need this to be switched on too. After you have installed Git Bash with the right options, you can install WSL Ubuntu 22.04.

Execute each command on Git Bash:

```bash
curl -o ~/ubuntu-base-22.04-base-amd64.tar.gz https://cdimage.ubuntu.com/ubuntu-base/releases/22.04/release/ubuntu-base-22.04-base-amd64.tar.gz
mkdir -p ~/wsl/ubuntu-22.04/instances
wsl --import ubuntu-22.04 ~/wsl/ubuntu-22.04/instances ~/ubuntu-base-22.04-base-amd64.tar.gz
rm ~/ubuntu-base-22.04-base-amd64.tar.gz
```

Then you can run Ubuntu 22.04 by executing
`wsl -d ubuntu-22.04`

If Git Bash freezes,  pseudo console support is not enabled. In such a case,
execute the `wsl -d ubuntu-22.04` command on Powershell. However you will not 
have all features you need to run cloudmesh smoothly. Instead we recommend to 
reinstall Git Bash with the proper options.
