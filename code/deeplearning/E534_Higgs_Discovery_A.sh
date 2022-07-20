#!/bin/sh
#SBATCH --job-name=E534_Higgs_Discovery_A.sh
#SBATCH --output=E534_Higgs_Discovery_A.log
#SBATCH --error=E534_Higgs_Discovery_A.error
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4GB
#SBATCH --time=3:00
#SBATCH -A bii_dsc_community

echo "# cloudmesh status=running progress=1 pid=${SLURM_JOB_ID}"

#module purge
#module load singularity
#
## Assuming that the container has been copied to the user's /scratch directory
## cp $CONTAINERDIR/tensorflow-2.8.0.sif /scratch/$USER
#CONTAINERDIR=/scratch/$USER
#echo `ls /home/$USER/experiment/E534_Higgs_Discovery_A`
#echo `which python`
#singularity run --nv $CONTAINERDIR/tensorflow-2.8.0.sif /home/atl9rn/experiment/E534_Higgs_Discovery_A/E534_Higgs_Discovery_A.py
##containerdir=$HOME
##singularity run --nv $containerdir/tensorflow-2.8.0.sif E534_Higgs_Discovery_A.py

python E534_Higgs_Discovery_A.py

echo " cloudmesh status=done progress=100 pid=${SLURM_JOB_ID}"
