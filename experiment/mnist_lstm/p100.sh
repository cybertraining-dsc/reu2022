#!/bin/sh
#SBATCH --job-name=p100.sh
#SBATCH --output=p100.log
#SBATCH --error=p100.error
#SBATCH --partition=gpu
#SBATCH --gres=gpu:p100:1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4GB
#SBATCH --time=3:00

echo "# cloudmesh status=running progress=1 pid=$SLURM_JOB_ID"

nvidia-smi
python mnist_lstm.py

echo "# cloudmesh status=done progress=100 pid=$SLURM_JOB_ID"
#
