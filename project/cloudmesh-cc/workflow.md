# Workflow 

The workflow class is a class in which users can upload files of jobs (bash and 
sbatch scripts) and then these jobs are loaded, saved, and run (and in doing so, 
images are produced of the workflow progression). 

This class was implemented with the intention of allowing users to upload jobs
that ranged in their complexity and necessary time to complete. Additionally, 
the python script was created with the intention that jobs could be run on 
various different operating systems (mac, Windows, and linux) and on different
computers, depending on the configuration that the user specified. 

For instance, if a user had four jobs that they wanted to run, but they wanted a
few of these jobs to be run on a remote computer (like UVa's Rivanna) and a few
to be run locally, they could split these tasks up and run them like that. They 
can run these jobs in parallel (meaning that the remote and local jobs are run 
at the same time) or they can run these in a topological sort fashion (which 
means that the workflow will wait for the preceding job to finish before the next
job is run). 

In this documentation, we will walk through the set up, methods, and use cases 
for this workflow and will mention the `fastAPI` service that accompanies this
as well. 

## Set-Up

### Cloning the repository

In order to be able to accurately access all of the componenets of the workflow
(specifically for using the python script for programming), it is necessary to 
navigate to [GitHub](https://github.com/cloudmesh/cloudmesh-cc) and clone the 
respository so that you can incorporate it into your own python scripts. The 
command looks like this: 

```bash
git clone <insert the git clone ssh link>
```

In doing so, you can pull the whole cloudmesh-cc repository into your own code 
development.

### Using the repository in your own code

Then, in you python script you would simply do the following:

```python
from cloudmesh.cc.workflow import workflow

w = workflow(name='workflow', filename='pathtoyamlyouhave')
```

### Yaml files

As you can see in the previous script, the workflow has a parameter called 
`filename`. This parameter is used to load the data that exists in a file into
the overal data structure that exists in the class. Essentially, this parameter 
is used to bring all of your data into the workflow so that it can be manipulated
and changed and used.

There are two options that exist for the instantiation of the workflow. One is 
that you can pre-build a script that the workflow can use to load in a bunch of 
data (hence the `filename` parameter from before). The other way is that you 
can manually add jobs (which will be discussed later on). First, let's discuss 
the set-up of a proper yaml file for the `workflow` to load in.

The yaml file should set up several parameters for the `workflow` to load in. 
Rather than explain, we will show an example. 

#### Example

```bash
workflow:
  nodes:
    start:
      label: start
      kind: local
      user: jacksonmiskill
      host: local
      status: ready
      progress: 0
      created: '2022-07-20 13:35:35.600053'
      modified: '2022-07-20 13:35:35.600053'
      script: null
      instance: null
      name: start
      parent: []
    end:
      label: end
      kind: local
      user: jacksonmiskill
      host: local
      status: ready
      progress: 0
      created: '2022-07-20 13:35:35.601217'
      modified: '2022-07-20 13:35:35.601217'
      script: null
      instance: null
      name: end
      parent:
      - job-local-2
```

Many of the methods within the `workflow` will update the yaml file with values, 
like the `created` and `modified` fields. There are several fields that are 
necessary to fill out before running, however, for the optimal functionality. 

First: the name parameter is where the `start` and `end` are above their fields.
It is necessary to fill this out with what you would like to run. This also used
in order to make sure that the data structure works as intended. 

`kind` it is necessary to fill out this field as well. This should specify where
you want the job to be run- it gives the `workflow` a flag to look for in deciding
which type of job to run. 

`name` is it also necessary to go ahead and write in the name of the job that you 
are attempting to instantiate. 

So, a basic script might look like this:

```bash
workflow:
  nodes:
    a:
      kind: local
      name: a
    b:
      kind: local
      name: b
```

This would be the most basic way to set this up. 


## Methods

The most important methods for this class are `jobs`, `load`, `add_job`, `add_dependencies`, `run_parallel`, `run_topo`, `remove_workflow`, `remove_job`, and `status`. 

These methods can be found on [GitHub](https://github.com/cloudmesh/cloudmesh-cc) and are, for the most part, self-explantory.

### Adding new jobs and dependencies 

One thing to point out here, however, is that you can manually add jobs and dependencies to the `workflow`, rather than only through the `yaml` file through the `add_job` and `add_dependencies` methods. 

To execute this in `python`, simply execute the following

```python
from cloudmesh.cc.workflow import Workflow

w = Workflow(name='workflow', filename='pathtoyaml')

w.add_job(name='job-x', label='job-x', kind='local', user='username', status='ready')

w.add_job(name='job-y', label='job-y', kind='local', user='username', status='ready')

w.add_dependencies(dependency='x-y')
```

### Running jobs

The `run_parallel` and `run_topo` methods are used in order to run the jobs that have been uploaded to the workflow data structure.The way that this works is simple. There are implementations of different kinds of the `job` object. This means that there is a `job` for `slurm`, for `local`, and for `ssh`. When the run method is called, it creates the correct type of job based on the kind of job as specified in the yaml file or in the `add_job` method. 

The `run_parallel` method runs the jobs side-by-side, if there are different kinds that are distinguished throughout the jobs. For instance, if there are two kinds of jobs in the workflow- one as `ssh` and one as `local`, then the `run_parallel` method will run them separately and bring them together. 

The `run_topo` method creates and runs jobs based on the topological sorting that the sorting method does. This method essentially creates a sort, and will wait for the preceding job to finish before the next job is run. 

### Removing Jobs

There are `remove_job` and `remove_workflow` methods that can be used to get rid of a single job, or the entirety of a workflow. 

In order to utilize `remove_job` is is necessary to specify the name of the job in the parameters. 

In order to utilize the `remove_workflow` is is necessary to specify the name of the workflow and then it should function as specified.