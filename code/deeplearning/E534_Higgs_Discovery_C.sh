#!/bin/sh
#SBATCH --job-name=E534_Higgs_Discovery_C.sh
#SBATCH --output=E534_Higgs_Discovery_C.log
#SBATCH --error=E534_Higgs_Discovery_C.error
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
#singularity run --nv $CONTAINERDIR/tensorflow-2.8.0.sif $HOME/experiment/E534_Higgs_Discovery_C/E534_Higgs_Discovery_C.py

python E534_Higgs_Discovery_C.py

echo " cloudmesh status=done progress=100 pid=$$"
