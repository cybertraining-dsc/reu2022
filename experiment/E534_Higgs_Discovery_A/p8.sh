#!/bin/sh
#SBATCH --job-name=p8.sh
#SBATCH --output=p8.log
#SBATCH --error=p8.error
#SBATCH --partition=gpu
#SBATCH --gres=gpu:p8:1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4GB
#SBATCH --time=3:00

echo "# cloudmesh status=running progress=1 pid=$SLURM_JOB_ID"

nvidia-smi
python E534_Higgs_Discovery_A.py

echo "# cloudmesh status=done progress=100 pid=$SLURM_JOB_ID"
#
