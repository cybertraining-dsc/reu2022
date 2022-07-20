#!/bin/sh
#SBATCH --job-name=mlp_mnist.sh
#SBATCH --output=mlp_mnist.log
#SBATCH --error=mlp_mnist.error
#SBATCH --partition=dev
#SBATCH --cpus-per-task=1
#SBATCH --mem=4GB
#SBATCH --time=3:00

echo "# cloudmesh status=running progress=1 pid=${SLURM_JOB_ID}"

module purge
module load singularity
CONTAINERDIR=/scratch/$USER
singularity run --nv $CONTAINERDIR/tensorflow-2.8.0.sif /home/atl9rn/experiment/E534_Higgs_Discovery_A/E534_Higgs_Discovery_A.py

#python mlp_mnist.py

echo " cloudmesh status=done progress=100 pid=${SLURM_JOB_ID}"