#!/bin/sh
#SBATCH --job-name=mnist_cnn.sh
#SBATCH --output=mnist_cnn.log
#SBATCH --error=mnist_cnn.error
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
#singularity run --nv $CONTAINERDIR/tensorflow-2.8.0.sif $HOME/experiment/mnist_cnn/mnist_cnn.py

python mnist_cnn.py

echo " cloudmesh status=done progress=100 pid=$$"