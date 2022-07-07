# Installing Cloudmesh Using Docker

## Installing Docker 

Docker is a platform that allows users to develop, publish, and run 
software applications in packages known as containers.

In order to install Docker, first go on Windows PowerShell and run as an 
Administrator and type in the following:

```
choco install docker-desktop -y
```

Next, make sure open Docker Desktop. Wait for the `Docker Desktop Starting` 
screen to finish. If it hasn't been done already, create a Docker account on 
their official website and log on to the account on the application after.

## Installing Cloudmesh

Next, go on Git Bash and create a directory called `cm` using the command:

```bash
cd ~
mkdir cm
```

Go into the `cm` directory and create the `cloudmesh-cc` folder using the 
following commands and let the folder install.

```bash
cd cm
git clone git@github.com:cloudmesh/cloudmesh-cc.git
```

## Installing Ubuntu with Docker

Using Git Bash, go into the docker directory using the command:

```bash
cd ~/cm/cloudmesh-cc/docker/cloudmesh
```

Now, install the `Make` tool using the command:

```bash
choco install make -y
```

After that's done, type in the command"

```bash
make image
```

If the host operating system of the user computer is Windows, type:

```bash
make wshell
```

If not, type:

```bash
make shell
```

This will switch the command line to Ubuntu


## Sources

* https://docs.docker.com/get-docker/
* https://docs.docker.com/get-started/
* https://docker-curriculum.com/
* https://github.com/cybertraining-dsc/reu2022/blob/main/project/git-bash-pseudo-console.md


