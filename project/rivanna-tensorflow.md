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

## Copying Tensorflow Container Image

## Loading Singularity Module

## Running Container Image

```nano
#!/bin/sh
#SBATCH --job-name=mlp_mnist.sh
#SBATCH --output=test.log
#SBATCH --error=test.error
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

# Assuming that the container has been copied to the user's /scratch directory
containerdir=$HOME
singularity run --nv $containerdir/tensorflow-2.8.0.sif mlp_mnist.py

echo " cloudmesh status=done progress=100 pid=$SLURM_JOB_ID"

#
```



## Sources

* https://docs.anaconda.com/anaconda/user-guide/tasks/tensorflow/
* https://www.rc.virginia.edu/userinfo/rivanna/software/tensorflow/
* https://www.rc.virginia.edu/userinfo/rivanna/software/containers/