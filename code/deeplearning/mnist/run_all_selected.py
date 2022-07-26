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


dryrun = False

exec = "sbatch"
exec = "python"
exec = "papermill"

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


print(user)
print(host)
print(gpu)
print(cpu)

tag = f"{host}-{user}-{cpu}-{gpu}"
print(tag)

if error:
  sys.exit()


scripts = textwrap.dedent("""
mlp_mnist
""").strip().splitlines()

# mnist_autoencoder
# mnist_cnn
# mnist_lstm
# mnist_mlp_with_lstm
# mnist_rnn
# mnist_with_distributed_training
# mnist_with_pytorch

for script in scripts:
  if exec == "papermill":
    output = f"{script}-output"
    command = f"{exec} {script}.ipynb {output}.ipynb"

  StopWatch.start(script)
  banner(command)
  if not dryrun:
    os.system(command)
  StopWatch.stop(script)


StopWatch.benchmark(sysinfo=False, tag=tag, node=host, user=user, filename=f"all-{tag}.log")



