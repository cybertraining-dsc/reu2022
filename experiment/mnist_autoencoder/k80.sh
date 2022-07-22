#!/bin/sh
#SBATCH --job-name=k80.sh
#SBATCH --output=k80.log
#SBATCH --error=k80.error
#SBATCH --partition=gpu
#SBATCH --gres=gpu:k80:1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4GB
#SBATCH --time=3:00

echo "# cloudmesh status=running progress=1 pid=$SLURM_JOB_ID"

nvidia-smi
python mnist_autoencoder.py

echo "# cloudmesh status=done progress=100 pid=$SLURM_JOB_ID"
#
