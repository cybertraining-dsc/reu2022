#!/bin/sh
#SBATCH --job-name=v100.sh
#SBATCH --output=v100.log
#SBATCH --error=v100.error
#SBATCH --partition=gpu
#SBATCH --gres=gpu:v100:1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4GB
#SBATCH --time=3:00

echo "# cloudmesh status=running progress=1 pid=$SLURM_JOB_ID"

nvidia-smi
python mlp_mnist.py

echo "# cloudmesh status=done progress=100 pid=$SLURM_JOB_ID"
#
