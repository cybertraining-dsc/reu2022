import os
import sys
import torch
import textwrap
import socket
import cpuinfo
from cloudmesh.common.Shell import Shell
from cloudmesh.common.util import banner
from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.variables import Variables
from cloudmesh.common.console import Console
from cloudmesh.common.systeminfo import os_is_windows
from cloudmesh.common.Shell import Shell
import time



dryrun = False

exec = "python"
exec = "papermill"
exec = "sbatch"

v = Variables()

user = v["user"] or Shell.sys_user().replace(' ', '_').replace('-', '_')
host = v["host"] or socket.gethostname().replace(' ', '_').replace('-', '_')
gpu = v["gpu"]
cpu = v["cpu"]
device = v["device"]

error = False

if user is None:
  Console.error("user not set")
  error = True

if host is None:
  Console.error("host not set")
  error = True

if cpu is None:
  Console.error("cpu not set")
  error = True

if gpu is None:
  Console.error("gpu not set")
  error = True

if device is None:
  Console.error("device not set")
  error = True


tag = f"{host}-{user}-{cpu}-{gpu}"

if error:
  sys.exit()


scripts = textwrap.dedent("""
mlp_mnist
mnist_autoencoder
""").strip().splitlines()

# mnist_cnn
# mnist_lstm
# mnist_mlp_with_lstm
# mnist_rnn
# mnist_with_distributed_training
# mnist_with_pytorch

cards = v['gpu']

if cards is None:
  cards = ['v100', 'a100', 'k80', 'p100', 'rtx-2080']
else:
  cards = v['gpu'].split(',')
for card in cards:
  for script in scripts:
    if exec == "papermill":
      output = f"{script}-output"
      command = f"{exec} {script}.ipynb {output}.ipynb"
    elif exec == 'sbatch':
      command = f"{exec} --gres=gpu:{card}:1 {script}.sh"
    v['host']='rivanna'
    v['gpu']=card

    banner(command)
    if not dryrun:
      sbatch = os.system(command)
    StopWatch.start(sbatch)

waiting_for_squeue = False
get_squeue = 'squeue -u $USER'
while waiting_for_squeue:
  r = os.system(get_squeue)
  if user in r:
    time.sleep(2)
    pass
  else:
    waiting_for_squeue = True
    break

StopWatch.stop(sbatch)

StopWatch.benchmark(sysinfo=False, tag=tag, node=host, user=user, filename=f"all-{tag}.log")




