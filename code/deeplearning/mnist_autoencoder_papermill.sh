#!/bin/sh
#SBATCH --job-name=mnist_autoencoder.sh
#SBATCH --output=mnist_autoencoder.log
#SBATCH --error=mnist_autoencoder.error
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4GB
#SBATCH --time=3:00

echo "# cloudmesh status=running progress=1 pid=$SLURM_JOB_ID"

nvidia-smi
source activate ENV3
papermill mnist_autoencoder.ipynb mnist_autoencoder_output.ipynb
nbcovert mnist_autoencoder_output.ipynb mnist_autoencoder_output.py

echo " cloudmesh status=done progress=100 pid=$SLURM_JOB_ID"

#
