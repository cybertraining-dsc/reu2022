#!/bin/sh
#SBATCH --job-name=E534_Higgs_Discovery_A.sh
#SBATCH --output=E534_Higgs_Discovery_A.log
#SBATCH --error=E534_Higgs_Discovery_A.error
#SBATCH --partition=gpu
#SBATCH --gres=gpu:v100:1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4GB
#SBATCH --time=3:00

echo "# cloudmesh status=running progress=1 pid=$$"

nvidia-smi --list-gpus
source activate ENV3
python E534_Higgs_Discovery_A.py

echo " cloudmesh status=done progress=100 pid=$$"#
