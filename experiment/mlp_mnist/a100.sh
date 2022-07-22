#!/bin/sh
#SBATCH --job-name=a100.sh
#SBATCH --output=a100.log
#SBATCH --error=a100.error
#SBATCH --partition=gpu
#SBATCH --gres=gpu:a100:1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4GB
#SBATCH --time=3:00

echo "# cloudmesh status=running progress=1 pid=$SLURM_JOB_ID"

nvidia-smi
python mlp_mnist.py

echo "# cloudmesh status=done progress=100 pid=$SLURM_JOB_ID"
#
