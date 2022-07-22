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
#SBATCH --partition=gpu
#SBATCH --gres=gpu:k80:1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4GB
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

## Examples from GitHub

Here we demonstrate how to run various examples from our GitHub:

Log into Rivanna

```bash
$ ssh rivanna
$rivanna: git clone https://github.com/cybertraining-dsc/reu2022.git
$rivanna: cd reu2022/code/deeplearning
$rivanna: bash test1.sh
```

Some users may want to generate modified `ipynb`'s to generate their
Python programs. In order to do so, you can simply say:

```bash
$rivanna: make all
```

Also, if you do not want to modify them, they are already included.

In case you would like to run an individual example, such as `mnist_autoencoder`,
you can it in the following way:

```bash
$rivanna: cd cm/reu2022/code/deeplearning
$rivanna: sbatch --gres:gpu:k80:1 mnist_autoencoder.sh
```

In case you would like to do Papermill, which allows you to run a Python
notebook directly without GUI, you can do it as follows:

```bash
$rivanna: pip install papermill
$rivanna: sbatch --gres:gpu:k80:1 mnist_autoencoder_papermill.sh
```

To see the results, all results are being prepended with a `# csv` string.
You can `fgrep` the result as follows:

```bash
$rivanna: fgrep '# csv' mnist_autoencoder_output.py
```

## Sources

* https://docs.anaconda.com/anaconda/user-guide/tasks/tensorflow/
* https://www.rc.virginia.edu/userinfo/rivanna/software/tensorflow/
* https://www.rc.virginia.edu/userinfo/rivanna/software/containers/