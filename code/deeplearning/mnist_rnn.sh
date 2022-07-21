#!/bin/sh
#SBATCH --job-name=mnist_rnn.sh
#SBATCH --output=mnist_rnn.log
#SBATCH --error=mnist_rnn.error
#SBATCH --partition=dev
#SBATCH --cpus-per-task=1
#SBATCH --mem=4GB
#SBATCH --time=3:00

echo "# cloudmesh status=running progress=1 pid=$$"

nvidia-smi
source activate ENV3
python mnist_rnn.py

echo " cloudmesh status=done progress=100 pid=$$"#
