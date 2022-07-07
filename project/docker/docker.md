# Running Ubuntu Through Cloudmesh and Docker

## Installing Docker with Chocolatey

Docker is a platform that allows users to develop, publish, and run 
software applications in packages known as containers.

In order to install Docker, first have Chocolatey installed. After it is 
installed, go on Windows PowerShell and run as an Administrator and type in 
the following:

```
choco install docker-desktop -y
```

If another host operating system is being used, go on the official Docker 
Desktop website and download the installation file from there.

Here is the link to the download website:
* https://docs.docker.com/get-docker/

Next, make sure open Docker Desktop. Wait for the `Docker Desktop Starting` 
screen to finish. If it hasn't been done already, create a Docker account on 
their official website and log on to the account on the application after.

## Installing Cloudmesh with Git Bash

Cloudmesh is a repository that can be downloaded and will be used to run 
Ubuntu on Docker. In order to download it, first, make sure Git Bash is 
downloaded so Unix commands can be run on non-Unix platforms through Bash. 
It's a good idea to download it specifically with Chocolatey and with Pseudo 
Console Support. [Instructions](https://github.com/cybertraining-dsc/reu2022/blob/main/project/git-bash-pseudo-console.md)
can be found in the Sources section. 

After Git Bash is installed, create a directory called `cm` using the command:

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

## Running Ubuntu with Docker

Using Git Bash, go into the docker directory using the following command. 
This will lead to the `docker/cloudmesh` directory under cloudmesh.

```bash
cd ~/cm/cloudmesh-cc/docker/cloudmesh
```

Now, install the `Make` tool using the command:

```bash
choco install make -y
```

This tool controls the generation of executables from the program. It helps 
builds and installs programs through the use of Makefiles. 

After `Make` is installed, it's a good idea to clean out any existing
containers and images in Docker that'll interfere with running Ubuntu. This 
can be done using the command:

```bash
make cleanall
```

After cleaning everything, Ubuntu and Python will be installed onto a Docker 
container, an isolated package of software exclusively on Docker. Unix 
commands are now possible to execute on Docker after installing Ubuntu. This 
process can take a while. In order to install, type in the following command:

```bash
make image
```

Wait for everything to install. This is where commands differ based on the 
user's host operating system. If Windows is used, type in the following 
command to start up Ubuntu from Git Bash.

```bash
make wshell
```

If Windows is not used, type in the following command:

```bash
make shell
```



Now, Ubuntu should be being run through Docker and Unix commands can now be 
executed. Because everything now takes place in Unix, a different directory 
now exists under Ubuntu. Due to that, type in the following command to be 
directed to `cloudmesh-cc` to that.

```ubuntu
pwd
cd ~
pwd
```

The following output should be produced. The first output shows the home 
host directory on Windows while the second output shows the Unix host
directory.

```
/home/USERNAME
/root
```

At this point, pytests of the various software modules of `cloudmesh-cc` can 
now be executed without having to worry about the host operating system. For 
example, in order to test out the `Job` class for `wsl` under the 
[file](https://github.com/cloudmesh/cloudmesh-cc/blob/main/cloudmesh/cc/job/wsl/Job.py),
type in the following command. All the tests should be able to pass. 

```ubuntu
cd cm/cloudmesh-cc
pytest -v -x --capture=no tests/test_job_wsl.py
```

## Running Ubuntu Remotely on Rivanna

In order to run Unix commands remotely, specifically Rivanna, the 
University of Virginia's Rivanna main supercomputing platform, first, have 
it installed. [Instructions](https://github.com/cybertraining-dsc/reu2022/blob/main/project/rivanna.md) 
for installation are provided under the Sources section. A UVA account with 
a computing ID must be created first.

After Rivanna is installed, open Cisco AnyConnect Secure Mobility Client and 
connect to the UVA Anywhere VPN.

After that, in any directory, type in the following:

```ubuntu
ssh-keygen
```

After the prompt shows up, press `ENTER` until all the prompts are through. 
Then, specifically type in the following:

```ubuntu
ssh-copy-id COMPID@rivanna.hpc.virginia.edu
```

A prompt will ask if the user wants to continue connecting. Type in "yes". 
After that, it will ask for the user's Rivanna password, type it in. Once 
that is done, the user is now connected to Rivanna through Docker.

## Sources

* https://docs.docker.com/get-docker/
* https://docs.docker.com/get-started/
* https://docker-curriculum.com/
* https://github.com/cybertraining-dsc/reu2022/blob/main/project/git-bash-pseudo-console.md
* https://github.com/cybertraining-dsc/reu2022/blob/main/project/rivanna.md


