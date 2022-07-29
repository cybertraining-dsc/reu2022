# Rivanna 

Rivanna is UVA's High Performance Computing (HPC) System. Rivanna
is used to run programs that require a lot of memory or computing
power. This tutorial will go through the basics of Rivanna, from
obtaining access to running specialized jobs.

## Table of Contents

* Rivanna
* Running Tensorflow on Rivanna
* Run Python MPI Programs on Rivanna
* Setting Parameters while Running `mnist` Jobs

![](images/learning.png) **Learning Objectives**

* Learn how to use Rivanna
* Learn how to set up VPN to access Rivanna from commandline
* Learn how to access Rivanna from a terminal including Windows

## Links

Here is a comprehensive list of useful links on how to navigate
the Rivanna system.

* Presentations
 
  * [Knuuti](https://docs.google.com/presentation/d/1Xt4kOtQpvl1JTDETJkOS-OMi8csZsJJw03xGus3QLA0/edit?usp=sharing)
  * [UVA Rivanna presentation, June 8th, 2022](https://learning.rc.virginia.edu/notes/rivanna-intro/)

* [Intro to Rivanna](https://learning.rc.virginia.edu/notes/rivanna-intro/)

* Rivanna Allocations: <https://www.rc.virginia.edu/userinfo/rivanna/allocations/>

* Rivanna Dashboard: <https://rivanna-portal.hpc.virginia.edu/pun/sys/dashboard>

Globus Transfer: <https://www.rc.virginia.edu/userinfo/globus/>

Rivanna SLURM Overview: <https://www.rc.virginia.edu/userinfo/rivanna/slurm/>

Queues Documentation: <https://www.rc.virginia.edu/userinfo/rivanna/queues/>

Documentation: <https://www.rc.virginia.edu/userinfo/rivanna/login/#web-based-access>

Login: <https://rivanna-portal.hpc.virginia.edu/>

UVA VPN: <https://in.virginia.edu/vpn>

Shell access: <https://rivanna-portal.hpc.virginia.edu/pun/sys/shell/ssh/rivanna.hpc.virginia.edu>

JupyterLab: <https://rivanna-portal.hpc.virginia.edu/pun/sys/dashboard/batch_connect/sys/jupyter_lab/session_contexts/new>

UVA HPC Support Email: hpc-support@virginia.edu

## Logging in to Rivanna via web interface

![UVA Login](images/uva-login.png)

**Figure:** UVA Login

The user must install Duo Mobile on smartphone to use as an 
authentication service to approve logins.

For security reasons we suggest never saving the password within
the browser autofill.

After logging in at <https://rivanna-portal.hpc.virginia.edu/>, 
you will receive an email through your UVA email inbox to create 
an account on Rivanna. Once completing the sign-up process, it 
will take around 1 hour for your account creation to be
finalized.

If connecting through SSH, then a VPN is required. Follow the
instructions to download UVA Anywhere at the following link:
<https://in.virginia.edu/vpn>

To log in to Rivanna, ensure you are connected to UVA Anywhere.
You will be prompted to enter your UVA password (not your ssh-key
password).
Issue the following (make sure you replace `abc123` with your
UVA id):

```bash
you@yourcomputer$ ssh-copy-id abc123@rivanna.hpc.virginia.edu 
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
abc123@rivanna.hpc.virginia.edu's password:

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'abc123@rivanna.hpc.virginia.edu'"
and check to make sure that only the key(s) you wanted were added.

you@yourcomputer$ ssh abc123@rivanna.hpc.virginia.edu
Last login: Tue May 31 11:55:43 2022
Authorized Use Only!
-bash-4.2$

```
## Notes: superpod

Estimated deployment for testing by the end of this summer. 

Hardware Components:

* 10 DGX-A100 (80GB) Servers (8 GPUs)
* 2 DGX-A100 (40GB) Servers (16 GPUs)
* HDR Infiniband (200GB/s) IB network fabric for GPU-to-GPU direct communication
* 500T ESS3200 pure SSD SpectrumScale (aka GPFS) direct-to-GPU storage array

The SuperPod is a collection of GPU servers (Nvidia DGX-A100) integrated into 
the Rivanna Cluster (on the GPU partition) with an 200Gb/s IB fabric 
interconnecting the GPUs with each other and with dedicated temporary storage for 
[Nvidia GPUDirect](https://developer.nvidia.com/gpudirect) features. The GPU Direct 
features allow for very fast transfers between the GPUs, storage and also for 
larger distributed GPU models.

## Special DGX Nodes on Rivanna

DGX A100 (udc-an36-1) is now available for your bii_dsc and bii_dsc_community members to test.

Here is the current status:

* The server is NOT YET integrated into the NVIDIA SuperPod because we are still awaiting networking equipment for implementing the SuperPod. We will be in 
  touch if there is a need for a maintenance outage to integrate the server into the SuperPod.
* There is a RAID0 array of NVMe disks mounted locally at /localscratch. The capacity is 27TB. Please keep in mind that /localscratch is not backed up.
* The server is named udc-an36-1 and is currently in the bii-gpu partition with a permanent reservation named bi_fox_dgx for only bii_dsc and 
  bii_dsc_community allocation members to use. To use this reservation for the A100 node, your researchers and students will have to use the following 
  slurm flags:

```
#SBATCH --reservation=bi_fox_dgx
#SBATCH --account=<enter relevant allocation here>
#SBATCH --partition=bii-gpu
#SBATCH --gres=gpu:<number of GPUs to request>
```

For -account, users will enter either bii_dsc or bii_dsc_community depending on which group they belong to. You can find this by running the allocations utility at the commandline. For -gres=gpu:, users should enter the number of GPUs requested.

The full details of the reservation are below. I named the Slurm reservation “bi_fox_dgx".  It’s not a typo.  To change the name of the reservation, I would have to delete the reservation and re-create it and the actual name of the reservation does not affect the reservation’s usability.  I’ve successfully tested the ability to use this reservation for all the current bii_dsc and bii_dsc_community members using the Slurm parameters I sent previously.

```
ReservationName=bi_fox_dgx StartTime=2022-06-01T08:37:38 EndTime=2022-06-02T08:37:38 Duration=1-00:00:00
   Nodes=udc-an36-1 NodeCnt=1 CoreCnt=256 Features=(null) PartitionName=bii-gpu Flags=DAILY,SPEC_NODES
   TRES=cpu=256
   Users=(null) Groups=(null) Accounts=bii_dsc,bii_dsc_community Licenses=(null) State=ACTIVE BurstBuffer=(null) Watts=n/a
   MaxStartDelay=(null)
```

### Starting interactive job on special partition

```\footnotesize
ssh $USERNAME@rivanna.hpc.virginia.edu

$ ijob --reservation=bi_fox_dgx --account bii_dsc --partition=bii-gpu --gres=gpu:1
salloc: Pending job allocation 39263336
salloc: job 39263336 queued and waiting for resources
salloc: job 39263336 has been allocated resources
salloc: Granted job allocation 39263336
salloc: Waiting for resource configuration
salloc: Nodes udc-an36-1 are ready for job

$ nvidia-smi 
```



which will result in
{\normalsize}


```
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 470.103.01   Driver Version: 470.103.01   CUDA Version: 11.4     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA A100-SXM...  Off  | 00000000:07:00.0 Off |                    0 |
| N/A   29C    P0    54W / 400W |     85MiB / 81251MiB |      0%      Default |
|                               |                      |             Disabled |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A     13486      G   /usr/bin/X                         63MiB |
|    0   N/A  N/A     13639      G   /usr/bin/gnome-shell               21MiB |
+-----------------------------------------------------------------------------+
```


## Activating Rivanna on GitBash

Once you have Rivanna installed locally on your computer with your account
set up, if you have Cloudmesh installed, you can simply connect to Rivanna on
the terminal using the following command. Make sure to run the terminal as
Admin or else it won't work. 

```bash
$ cms vpn connect
```

In order to disconnect from Rivanna, simply use the command:

```bash
$ cms vpn disconnect
```

## Installing Python 3.10.5 on Rivanna with ENV3

After you log in into Rivanna, there's a chance you're running Rivanna on an
outdated version of Python, restricting you from being able to run Python
files properly. In order to do so, you'll need a fully to up-to-date version
of Python with the ENV3 virtual environment.

### Activate Python3

First Python3, must be activated and can be done by typing in the following:

```bash
$ ssh rivanna
rivanna$ module load cuda cudnn
rivanna$ module load anaconda
rivanna$ conda create -n ENV3  -c conda-forge python=3.10.5
```

The last command may take a while. After it's done installing, activate the 
ENV3 virtual environment of Python 3.10.5 by typing in:

```bash
rivanna$ source activate ENV3
```


### .bashrc

Now, you must open your `.bashrc` file. If it doesn't exist, create one.
Using any editor, open it and copy and paste the following: 

```bash
# Source global definitions
if [ -f /etc/bashrc ]; then
    . /etc/bashrc
fi


PS1="\s-\v\$"
alias vi='vim'
module load cuda cudnn
module load anaconda
source activate ENV3
```

### Installing Cloudmesh into Rivanna

Once Python 3.10.5 is installed with the ENV3 virutal environment. Cloudmesh
can now be installed by first making a `cm` directory, installing the
Cloudmesh Installer through pip and using the installer to get the Cloudmesh
files into the `cm` directory. All of this can be done using the following 
commands:

```bash
$ mkdir cm
$ cd cm
$ pip install cloudmesh-installer
$ cloudmesh-installer --ssh get cc
$ cloudmesh-installer --ssh get cms
```

If the last command doesn't work due to access rights, type in:

```bash
$ cloudmesh-installer get cc
$ cloudmesh-installer get cms
```

### Example Script for Using GPUs

Slurm jobs can be run in Rivanna through `sbatch` scripts. Various arguments
such as the job, output, GPU, time, account, etc. can be specified as shown
in the example script below. 

```
#!/usr/bin/env bash
#SBATCH --job-name=mydemojob
#SBATCH --output=%u-%j.out
#SBATCH --error=%u-%j.err
#SBATCH --partition=gpu
#SBATCH -c 1
#SBATCH --gres="gpu:v100:1"
#SBATCH --mem=4GB
#SBATCH --time=3:00
#SBATCH --account=c4gc

# your automation code here..
python mydemojob.py
```

### How Do You Activate Different GPUs

In the `sbatch` scripts, different GPUs can be activated by specifying it 
through `gres` argument. 

```
#SBATCH --gres="gpu:p100:1"
#SBATCH --gres="gpu:v100:1"
#SBATCH --gres="gpu:k80:1"
#SBATCH --gres="gpu:a100:1"
#SBATCH --gres="gpu:a100:1"
#SBATCH --gres="gpu:rtx2080:1"
```

* TODO: How can we use a100 w/ 40 GB vs. 80 GB?
* TODO: How can we use Gregor's special a100?


## Allocations

The time you spend on Rivanna is allocated as Service Units (SUs) into the
account you're using. When you type in the following command:

```bash
$ allocations
```

The results show you which accounts you're currently under and the amount of 
SUs is in balance, reserved, and available as shown below. 

```
Account                      Balance        Reserved       Available
-----------------          ---------       ---------       ---------
xyz_community                  99999               0           99999
comp4gc                       146527               0          146527
```

You are also able to access the information of all the users under the accounts
you're under by typing in the following command:

```bash
$rivanna allocations -a comp4gc
```

## SSH Config

SSH Config makes it easier for users to connect to Rivanna by specifying 
arguments in the `config` file instead of typing it in the terminal.

The `.ssh` directory and `config` file can be created using the following
commands:

```bash
$rivanna mkdir -p ~/.ssh && chmod 700 ~/.ssh
$rivanna touch ~/.ssh/config
$rivanna chmod 600 ~/.ssh/config
```

The `config` can then be edited using any terminal text editor of your choice,
using the following command. Nano is used in this example.

```bash
$rivanna nano ~/.ssh/config
```

Inside the `config` file, copy and paste the following:

```
host rivanna
        User <USERNAME>
        HostName rivanna.hpc.virginia.edu
        IdentityFile ~/.ssh/id_rsa
```

## Links

* [ssh Config File](<https://linuxize.com/post/using-the-ssh-config-file/>)
* [Knuuti](https://docs.google.com/presentation/d/1Xt4kOtQpvl1JTDETJkOS-OMi8csZsJJw03xGus3QLA0/edit?usp=sharing)
* [UVA Rivanna presentation, June 8th, 2022](https://learning.rc.virginia.edu/notes/rivanna-intro/)