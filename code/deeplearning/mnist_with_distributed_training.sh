#!/bin/sh
#SBATCH --job-name=mnist_with_distributed_training.sh
#SBATCH --output=mnist_with_distributed_training.log
#SBATCH --error=mnist_with_distributed_training.error
#SBATCH --partition=dev
#SBATCH --cpus-per-task=1
#SBATCH --mem=4GB
#SBATCH --time=3:00

echo "# cloudmesh status=running progress=1 pid=$$"

module purge
module load singularity

# Assuming that the container has been copied to the user's /scratch directory
CONTAINERDIR=$HOME
singularity run --nv $CONTAINERDIR/tensorflow-2.8.0.sif $HOME/experiment/mnist_with_distributed_training/mnist_with_distributed_training.py

#python mnist_with_distributed_training.py

echo " cloudmesh status=done progress=100 pid=$$"#
