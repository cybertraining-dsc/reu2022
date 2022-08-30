# Issues

Cloudmesh contains a convenient program to list all issues of
repositories downloaded in the current directory. The command can be
installed with

```bash
$ pip install cloudmesh-git
```

alternatively you can simply install it from source with 

```bash
$ cd cm
$ git clone git@github.com:cloudmesh/cloudmesh-git.git
$ cd cloudmesh-git 
$ pip install -e .
$ cd ..
```

To run it cd to the directory where all your git repos are located
and say

```bash
$ cms git issues --repo=. --refresh
```

This will open a Web page that list all issues across all repos
in that directory.

In case you like to see all issues only for the REU2022, please check out
the [GitHub Link](https://github.com/cloudmesh/cloudmesh-cc/issues).


To get all issues for cloudmesh projects that interest you, you can create an issue list from 
selected repositories.

For example you can checkout the following

```bash
$ cd cm
$ cloudmesh-installer get cmd5
$ git clone git@github.com:cloudmesh/yamldb.git
$ git clone git@github.com:cloudmesh/cloudmesh-git.git
$ git clone git@github.com:cloudmesh/cloudmesh-catalog.git
$ git clone git@github.com:cloudmesh/cloudmesh-data.git
$ git clone git@github.com:cloudmesh/cloudmesh-sbatch.git
$ git clone git@github.com:cloudmesh/cloudmesh-mpi.git
$ git clone git@github.com:cloudmesh/cloudmesh-slurm.git
$ git clone git@github.com:cloudmesh/cloudmesh-pi-burn.git
$ git clone git@github.com:cloudmesh/cloudmesh-pi-cluster.git
$ git clone git@github.com:cloudmesh-community/book.git
$ git clone git@github.com:cybertraining-dsc/reu.git
$ git clone git@github.com:cyberaide/bookmanager.git
```

To get the list use

```bash
$ cms git issues --repo=reu --refresh
```