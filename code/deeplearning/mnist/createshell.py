import glob

script = '''#!/bin/sh
#SBATCH --job-name={name}.sh
#SBATCH --output={name}.log
#SBATCH --error={name}.error
#SBATCH --partition=gpu
#SBATCH --cpus-per-task=1
#SBATCH --mem=4GB
#SBATCH --time=3:00

echo "# cloudmesh status=running progress=1 pid=$$"

nvidia-smi --list-gpus
source activate ENV3
python {name}.py

echo " cloudmesh status=done progress=100 pid=$$"#
'''

for file in glob.glob('*.ipynb'):
        name = file.replace('.ipynb', '')
        f = open(f'{name}.sh', 'w')
        f.write(script.format(name=name))
        f.close()