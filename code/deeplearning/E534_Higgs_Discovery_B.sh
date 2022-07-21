#!/bin/sh
#SBATCH --job-name=E534_Higgs_Discovery_B.sh
#SBATCH --output=E534_Higgs_Discovery_B.log
#SBATCH --error=E534_Higgs_Discovery_B.error
#SBATCH --partition=dev
#SBATCH --cpus-per-task=1
#SBATCH --mem=4GB
#SBATCH --time=3:00

echo "# cloudmesh status=running progress=1 pid=$$"

nvidia-smi
source activate ENV3
python E534_Higgs_Discovery_B.py

echo " cloudmesh status=done progress=100 pid=$$"#
