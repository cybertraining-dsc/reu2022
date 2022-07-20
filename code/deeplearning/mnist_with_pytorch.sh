#!/bin/sh
#SBATCH --job-name=mnist_with_pytorch.sh
#SBATCH --output=mnist_with_pytorch.log
#SBATCH --error=mnist_with_pytorch.error
#SBATCH --partition=dev
#SBATCH --cpus-per-task=1
#SBATCH --mem=4GB
#SBATCH --time=3:00

echo "# cloudmesh status=running progress=1 pid=$$"

module load cuda cudnn
module load anaconda
source activate ENV3

python mnist_with_pytorch.py

echo " cloudmesh status=done progress=100 pid=$$"#
