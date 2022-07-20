#!/bin/sh
#SBATCH --job-name=google_colab_mnist_example.sh
#SBATCH --output=google_colab_mnist_example.log
#SBATCH --error=google_colab_mnist_example.error
#SBATCH --partition=dev
#SBATCH --cpus-per-task=1
#SBATCH --mem=4GB
#SBATCH --time=3:00

echo "# cloudmesh status=running progress=1 pid=$$"

module load cuda cudnn
module load anaconda
source activate ENV3

python google_colab_mnist_example.py

echo " cloudmesh status=done progress=100 pid=$$"#
