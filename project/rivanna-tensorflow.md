# Running Tensorflow on Rivanna

---

![](images/learning.png) **Learning Objectives**

* Learn how to properly install Tensorflow on Rivanna using `conda`
* Learn how to load a singularity module of Tensorflow
* Learn how to run the GPU container image of Tensorflow through `sbatch`

---


## Activating Rivanna

Once you have Rivanna installed locally on your computer with your account
set up, if you have Cloudmesh installed, you can simply connect to Rivanna on
GitBash using the following commands. Make sure to run the terminal as
Admin or else the first command won't work. 

```bash
$ cms vpn connect
$ ssh rivanna
```

## Installing Tensorflow Using Conda

Generally in Rivanna, Python is run in a Conda environment. Because of that,
Tensorflow can be installed using Conda using the command:

```
$rivanna conda install -n ENV3 tensorflow-gpu cudatoolkit
```

## Loading and Running Singularity

Alternatively, you can use Rivanna's built-in containers for running Tensor-
flow called Singularity. You can load using the following commands:

```bash
rivanna$ module load singularity
rivanna$ module load tensorflow/2.8.0
```

This will give you this output which you can run:

```
To execute the default application inside the container, run:
singularity run --nv $CONTAINERDIR/tensorflow-2.8.0.sif
```

You should get instructions on how to now run this Tensorflow container. The `--nv`
flag is to load the NVIDIA graphic driver for use of GPU.

## Copying Tensorflow Container Image

Before running Tensorflow on any file, you first want to copy the Tensorflow
container image into your personal home directory. This can be done by typing in
the following commands:

```bash
rivanna$ module load singularity
rivanna$ module load tensorflow/2.8.0
rivanna$ cd $CONTAINERDIR
rivanna$ cp tensorflow-2.8.0.sif $HOME
```

The first two commands loads you into the Singularity Tensorflow container. 
You are then directed to the default location of the container image and then
you copy the image file into your home directory.

## Running the Singularity Shell

Before you run this shell, make sure to install cloudmesh in the image. Run the
following commands:

```bash
rivanna$ singularity shell $HOME/tensorflow-2.8.0.sif
Singularity> pip install cloudmesh-common
```


## Running Slurm Jobs

Slurm jobs can be run through the Tensorflow container through `sbatch` scripts. 
Various arguments such as the job, output, GPU, time, account, etc. can be 
specified as shown in the example script below. 

```nano
#!/bin/sh
#SBATCH --job-name=mydemojob
#SBATCH --output=%u-%j.out
#SBATCH --error=%u-%j.err
#SBATCH --partition=dev
#SBATCH --cpus-per-task=1
#SBATCH --mem=4GB
#SBATCH -p gpu
#SBATCH --gres=gpu:1
#SBATCH -t 00:01:00
#SBATCH -A bii_dsc_community

echo "# cloudmesh status=running progress=1 pid=$SLURM_JOB_ID"

module purge
module load singularity

containerdir=$HOME
singularity run --nv $containerdir/tensorflow-2.8.0.sif mydemojob.py

echo " cloudmesh status=done progress=100 pid=$SLURM_JOB_ID"

#
```



## Sources

* https://docs.anaconda.com/anaconda/user-guide/tasks/tensorflow/
* https://www.rc.virginia.edu/userinfo/rivanna/software/tensorflow/
* https://www.rc.virginia.edu/userinfo/rivanna/software/containers/