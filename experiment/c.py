import glob

script = '''#!/bin/sh
#SBATCH --job-name={gpu}.sh
#SBATCH --output={gpu}.log
#SBATCH --error={gpu}.error
#SBATCH --partition=gpu
#SBATCH --gres=gpu:{gpu}:1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4GB
#SBATCH --time=3:00

echo "# cloudmesh status=running progress=1 pid=$SLURM_JOB_ID"

nvidia-smi
python {name}.py

echo "# cloudmesh status=done progress=100 pid=$SLURM_JOB_ID"
#
'''

f = open("programs.txt",'r')
lines = f.readlines()
f.close()

for name in lines:
    name = name.replace("\n","")
    for gpu in ["p8","k80","a100","v100","p100"]:
        s = open(f'{name}/{gpu}.sh', 'w')
        s.write(script.format(name=name,gpu=gpu))
        s.close()
