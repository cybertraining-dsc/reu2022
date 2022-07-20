#!/bin/sh
#SBATCH --job-name=python_warmup.sh
#SBATCH --output=python_warmup.log
#SBATCH --error=python_warmup.error
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
#singularity run --nv $CONTAINERDIR/tensorflow-2.8.0.sif $HOME/experiment/python_warmup/python_warmup.py

python python_warmup.py

echo " cloudmesh status=done progress=100 pid=$$"
