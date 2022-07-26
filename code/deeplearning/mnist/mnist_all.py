from cloudmesh.common.Shell import Shell
from cloudmesh.common.util import banner
from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.variables import Variables
from cloudmesh.common.console import Console
import textwrap

exec = "sbatch"
exec = "python"
exec = "papermill"

v = Variables()

user = v["user"]
host = v["host"]
gpu = v["gpu"]
cpu = v["cpu"]
device = v["device"]


if user is None:
  Console.error("user not set")

if host is None:
  Console.error("host not set")

if cpu is None:
  Console.error("cpu not set")

if gpu is None:
  Console.error("gpu not set")

if device is None:
  Console.error("device not set")



scripts = textwrap.dedent("""
mlp_mnist
mnist_autoencoder
mnist_cnn
mnist_lstm
mnist_mlp_with_lstm
mnist_rnn
mnist_with_distributed_training
mnist_with_pytorch""").strip().splitlines()


for script in scripts:
  if exec == "papermill":
    output = f"{script}-output"
    command = f"{exec} {script}.ipynb {output}.ipynb"

  StopWatch.start(script)
  banner(command)
  StopWatch.stop(script)


StopWatch.benchmark(sysinfo=False)



