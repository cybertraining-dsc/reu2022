import textwrap
import os
from cloudmesh.common.variables import Variables

exec = 'python'
# exec = 'sbatch'

v = Variables()
host = v('host')
user = v('user')
cpu = v('cpu')
gpu = v('gpu')

log = f'{host}-{user}-{cpu}-{gpu}.log'

scripts=textwrap.dedent('''
mlp_mnist.sh
mnist_autoencoder.sh
mnist_cnn.sh
mnist_lstm.sh
mnist_mlp_with_lstm.sh
mnist_rnn.sh
mnist_with_distributed_training.sh
mnist_with_pytorch.sh
''').strip().splitlines()

os.system(f'rm -f {log}')
os.system(f'touch {log}')

for script in scripts:
    os.system(f'{exec} {script} >> {log}')



