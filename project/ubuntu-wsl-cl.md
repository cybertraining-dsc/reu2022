# How to Install WSL Ubuntu 22.04 on Command Line

Execute each command on Git Bash:

```bash
curl -o ~/ubuntu-base-22.04-base-amd64.tar.gz https://cdimage.ubuntu.com/ubuntu-base/releases/22.04/release/ubuntu-base-22.04-base-amd64.tar.gz
mkdir -p ~/wsl/ubuntu-22.04/instances
wsl --import ubuntu-22.04 ~/wsl/ubuntu-22.04/instances ~/ubuntu-base-22.04-base-amd64.tar.gz
rm ~/ubuntu-base-22.04-base-amd64.tar.gz
```

Then you can run Ubuntu 22.04 by executing
`wsl -d ubuntu-22.04`

Git Bash may freeze if pseudo console support is not enabled. In such a case,
execute the `wsl -d ubuntu-22.04` command on Powershell.