#!/bin/sh
#SBATCH --job-name=mnist_autoencoder.sh
#SBATCH --output=mnist_autoencoder.log
#SBATCH --error=mnist_autoencoder.error
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
#singularity run --nv $CONTAINERDIR/tensorflow-2.8.0.sif $HOME/experiment/mnist_autoencoder/mnist_autoencoder.py

python mnist_autoencoder.py

echo " cloudmesh status=done progress=100 pid=$$"