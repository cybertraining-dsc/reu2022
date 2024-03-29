#!/bin/sh
#SBATCH --job-name=mlp_mnist.sh
#SBATCH --output=mlp_mnist.log
#SBATCH --error=mlp_mnist.error
#SBATCH --partition=gpu
#SBATCH --cpus-per-task=1
#SBATCH --mem=8GB
#SBATCH --time=15:00

echo "# cloudmesh status=running progress=1 pid=$$"

nvidia-smi --list-gpus
cd ~
source activate ENV3
python mlp_mnist.py

echo "# cloudmesh status=done progress=100 pid=$$"
