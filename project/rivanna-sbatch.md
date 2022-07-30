# Run Python MPI programs on Rivanna

---

**Learning Objectives**

* Learn how to submit Slurm jobs on Rivanna through SBATCH
* Learn how to run SBATCH through Bash files
* Learn how view the queue of running Slurm jobs

---

## SBATCH in Bash Files

SBATCH is a way to submit jobs onto Rivanna's compute nodes. With any call,
there must be specifications for the job. Take this example `mlp_mnist.sh`
file, which runs a python program `mlp_mnist.py`.

```bash
#!/bin/sh
#SBATCH --job-name=mlp_mnist.sh
#SBATCH --output=mlp_mnist_%A.log
#SBATCH --error=mlp_mnist_%A.error
#SBATCH --partition=gpu
#SBATCH --gres=gpu:k80:1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4GB
#SBATCH --time=3:00

echo "# cloudmesh status=running progress=1 pid=$SLURM_JOB_ID"

nvidia-smi
source activate ENV3
python mlp_mnist.py

echo "# cloudmesh status=done progress=100 pid=$SLURM_JOB_ID"
#
```

The name of the `.sh` file, as well as the output and error files are
specified with the first three `#SBATCH` lines. The `.log` and `.error`
files are additionally marked with `%A`, which will be replaced with
the job's unique id.

The `--partition` specifies which queue the job will enter and thus the type
of resources it is allowed. More information can be seen in @fig:slurm-partitions.

```![Slurm partitions](images/partitions.png){#fig:slurm-partitions}```

The `--gres` is used for jobs that use the GPU. The last number specifies
the number of cores and the middle specifies which GPU will be used. It can
be left blank to use the default. Some GPUs are *A100, V100, K80, P100,* and
*P8.* 

The `--cpus-per-task` and `--mem` specify the CPUs and memory to be allocated,
and the `--time` sets the max time allowed for Rivanna to complete the task,
or else it will stop. For `gpu` partitioned jobs, this can be up to three days.

## Running in SBATCH

To run this bash file `mlp_mnist.sh`, use this command:

```bash
rivanna $ sbatch mlp_mnist.sh
```

This submits the job to the partition, and it can be watched with either of
the following commands:

`watch squeue -u ${USER}` or `squeue -u ${USER}`

These commands pull up all the jobs you have submitted. "Watching" will refresh
this list every 2 seconds and can be exited with `Ctrl-C`. When the job has
finished, there should be associated `.error` and `.log` files specified with
the `#SBATCH` commands.

This specific bash file includes the `nvidia-smi` command which pulls up a chart
with the NVIDIA GPU specifications. For example, here are the P8 details.

```
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 470.103.01   Driver Version: 470.103.01   CUDA Version: 11.4     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA GeForce ...  Off  | 00000000:62:00.0 Off |                  N/A |
| 29%   25C    P8    11W / 250W |      7MiB / 11019MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
```


## mlp_mnist.sh

```bash
#!/bin/sh
#SBATCH --job-name=mlp_mnist.sh
#SBATCH --output=mlp_mnist_%A.log
#SBATCH --error=mlp_mnist_%A.error
#SBATCH --partition=gpu
#SBATCH --gres=gpu:k80:1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4GB
#SBATCH --time=3:00

# A100, V100, K80, P100: set in gres
echo "# cloudmesh status=running progress=1 pid=$SLURM_JOB_ID"

#module purge
#module load singularity

## Assuming that the container has been copied to the user's /scratch directory
#CONTAINERDIR=$HOME
#singularity run --nv $CONTAINERDIR/tensorflow-2.8.0.sif $HOME/experiment/mlp_mnist/mlp_mnist.py

nvidia-smi
# pip install cloudmesh-common
source activate ENV3
which python
python -V
python mlp_mnist.py

echo "# cloudmesh status=done progress=100 pid=$SLURM_JOB_ID"
#
```

### Makefile

```
IMAGE=tensorflow-2.8.0
image:
        cp ${IMAGE}.sif ${IMAGE}-cms.sif
        singularity exec ${IMAGE}-cms.sif pip install cloudmesh-common -U

mlp_mnist:
        cd experiment/mlp_mnist; sbatch mlp_mnist.sh

watch:
        watch squeue -u ${USER}

cat:
        cd experiment/mlp_mnist; cat *.error *.log
```


#### Time for GPUs

| GPU  | # Cores | Time to run mlp_mnist.sh |
|:-----|:--------|:-------------------------|
| P8   | 1       | 16.521 seconds           |
| K80  | 1       | 40.519 seconds           |
| A100 | 1       | 24.557 seconds           |
| V100 | 1       | 21.811 seconds           |
| P100 | 1       | 31.927 seconds           |