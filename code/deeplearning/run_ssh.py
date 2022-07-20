import os
import shutil
import time

from cloudmesh.cc.job.ssh.Job import Job

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

# jobs = ["E534_Higgs_Discovery_A"]
jobs = ["mlp_mnist"]

# https://stackoverflow.com/questions/32538758/nameerror-name-get-ipython-is-not-defined


for script in jobs:
    pyfile = Job(name=script, host=host, username=username, type="python")
    # print(pyfile)
    pyfile.sync()
    # s, l, e = pyfile.run()
    # pyfile.watch()

    job = Job(name=script, host=host, username=username)
    print(job)
    job.sync()
    s, l, e = job.run()
    job.watch(20)

    print("State:", s)
    print("Log:", l)
    print("Error:", e)
    # log = job.get_log()
    # print("Log:",log)
    # progress = job.get_progress()
    # print("Progress:", progress)
    # status = job.get_status(refresh=True)
    # print("Status:", status)
    # parent, child = job.kill(period=2)