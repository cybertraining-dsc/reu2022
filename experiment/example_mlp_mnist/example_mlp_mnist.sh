#!/bin/sh
#SBATCH --job-name=example_mlp_mnist.sh
#SBATCH --output=example_mlp_mnist.log
#SBATCH --error=example_mlp_mnist.error
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
#singularity run --nv $CONTAINERDIR/tensorflow-2.8.0.sif $HOME/experiment/example_mlp_mnist/example_mlp_mnist.py

python example_mlp_mnist.py

echo " cloudmesh status=done progress=100 pid=$$"
