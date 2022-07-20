import os
import shutil
import time

from cloudmesh.cc.job.ssh.Job import Job
from cloudmesh.cc.workflow import Workflow

from cloudmesh.common.Shell import Shell
from cloudmesh.common.util import path_expand
from cloudmesh.common.variables import Variables

variables = Variables()

if "host" not in variables:
    host = "rivanna.hpc.virginia.edu"
else:
    host = variables["host"]

if "username" in variables:
    username = variables["username"]
else:
    username = os.path.basename(os.environ["HOME"])

try:
    r = Shell.run(f"ssh {username}@{host} hostname")
    login_success = "Could not resolve hostname" not in r
    if "'s password:" in r:
        print('if statement worked')
except:  # noqa: E722
    login_success = False


#
# Jobs to run
#

jobs = ["E534_Higgs_Discovery_A","E534_Higgs_Discovery_B","E534_Higgs_Discovery_C","E534_Higgs_Discovery_D"]
# jobs = ["mlp_mnist"]
w = Workflow()

for script in jobs:
    pyfile = Job(name=script, host=host, username=username, type="python")
    # print(pyfile)
    pyfile.sync()
    # s, l, e = pyfile.run()
    # pyfile.watch()

    job = Job(name=script, host=host, username=username)
    print(job)
    # w.add_job(job)
    job.sync()
    s, l, e = job.run()
    job.watch(30)

    print("State:", s)
    print("Log:", l)

    # deletes error file if empty and prints if there is an error
    if os.path.getsize(f"{script}.error") == 0:
        Shell.run(f"rm {script}.error")
    else:
        print("Error:", e)

    # progress = job.get_progress()
    # print("Progress:", progress)
    # status = job.get_status(refresh=True)
    # print("Status:", status)
    # parent, child = job.kill(period=2)