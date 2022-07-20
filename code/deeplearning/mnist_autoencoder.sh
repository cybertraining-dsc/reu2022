#!/bin/sh
#SBATCH --job-name=mnist_autoencoder.sh
#SBATCH --output=mnist_autoencoder.log
#SBATCH --error=mnist_autoencoder.error
#SBATCH --partition=dev
#SBATCH --cpus-per-task=1
#SBATCH --mem=4GB
#SBATCH --time=3:00

echo "# cloudmesh status=running progress=1 pid=$$"

module load cuda cudnn
module load anaconda
source activate ENV3

python mnist_autoencoder.py

echo " cloudmesh status=done progress=100 pid=$$"#
