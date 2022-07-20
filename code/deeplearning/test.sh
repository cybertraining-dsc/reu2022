#!/bin/sh
#SBATCH --job-name=mlp_mnist.sh
#SBATCH --output=test.log
#SBATCH --error=test.error
#SBATCH --partition=dev
#SBATCH --cpus-per-task=1
#SBATCH --mem=4GB
#SBATCH --time=3:00

echo "# cloudmesh status=running progress=1 pid=${SLURM_JOB_ID}"

module purge
module load singularity
CONTAINERDIR=$HOME
singularity run --nv $CONTAINERDIR/tensorflow-2.8.0.sif /home/$USER/cm/reu2022/code/deeplearning/mlp_mnist.py

echo " cloudmesh status=done progress=100 pid=${SLURM_JOB_ID}"
