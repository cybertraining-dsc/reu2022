#!/bin/sh
#SBATCH --job-name=E534_Higgs_Discovery_C.sh
#SBATCH --output=E534_Higgs_Discovery_C.log
#SBATCH --error=E534_Higgs_Discovery_C.error
#SBATCH --partition=gpu
#SBATCH --gres=gpu:v100:1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4GB
#SBATCH --time=3:00

echo "# cloudmesh status=running progress=1 pid=$$"

nvidia-smi --list-gpus
source activate ENV3
python E534_Higgs_Discovery_C.py

echo " cloudmesh status=done progress=100 pid=$$"#
