#!/bin/sh
#SBATCH --job-name=google_colab_mnist_example.sh
#SBATCH --output=google_colab_mnist_example.log
#SBATCH --error=google_colab_mnist_example.error
#SBATCH --partition=dev
#SBATCH --cpus-per-task=1
#SBATCH --mem=4GB
#SBATCH --time=3:00

echo "# cloudmesh status=running progress=1 pid=$$"

#module purge
#module load singularity
#
## Assuming that the container has been copied to the user's /scratch directory
#CONTAINERDIR=$HOME
#singularity run --nv $CONTAINERDIR/tensorflow-2.8.0.sif $HOME/experiment/google_colab_mnist_example/google_colab_mnist_example.py

python google_colab_mnist_example.py

echo " cloudmesh status=done progress=100 pid=$$"