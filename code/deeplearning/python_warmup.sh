#!/bin/sh
#SBATCH --job-name=python_warmup.sh
#SBATCH --output=python_warmup.log
#SBATCH --error=python_warmup.error
#SBATCH --partition=gpu
#SBATCH --gres=gpu:v100:1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4GB
#SBATCH --time=3:00

echo "# cloudmesh status=running progress=1 pid=$$"

nvidia-smi
source activate ENV3
python python_warmup.py

echo " cloudmesh status=done progress=100 pid=$$"#
