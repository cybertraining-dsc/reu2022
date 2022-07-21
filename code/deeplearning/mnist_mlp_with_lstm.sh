#!/bin/sh
#SBATCH --job-name=mnist_mlp_with_lstm.sh
#SBATCH --output=mnist_mlp_with_lstm.log
#SBATCH --error=mnist_mlp_with_lstm.error
#SBATCH --partition=dev
#SBATCH --cpus-per-task=1
#SBATCH --mem=4GB
#SBATCH --time=3:00

echo "# cloudmesh status=running progress=1 pid=$$"

nvidia-smi
source activate ENV3
python mnist_mlp_with_lstm.py

echo " cloudmesh status=done progress=100 pid=$$"#
