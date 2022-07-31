# Setting Parameters while Running `mnist` Jobs

---

## Table of Contents

* Rivanna
* Running Tensorflow on Rivanna
* Run Python MPI Programs on Rivanna
* Setting Parameters while Running `mnist` Jobs

---

![](images/learning.png) **Learning Objectives**

* Learn how to set user parameters using `cms`
* Learn how to properly name the `user`, `host`, `cpu`, `gpu`, and `device`
parameters
* Learn how run the `mnist` files and view the status of their progress

---

## Having Cloudmesh Installed

First, make sure Cloudmesh is installed properly on your local device. This can
be done with the following command:

```bash
$ pip install cloudmesh-installer
$ mkdir cm
$ cd cm
$ cloudmesh-installer --ssh get cc
```
## Installing the `reu2022` folder

Next, make sure the `reu2022` folder is installed. While you're in the `cm` 
folder, do the following commands to install the folder and be directed to the
`mnist` folder.

```bash
$ git clone https://github.com/cybertraining-dsc/reu2022.git
$ cd reu2022/code/deeplearning/mnist
```

## Setting the `user`, `host` parameters

Now, in order to run these jobs, the following parameters must be set: `user`,
`host`, `cpu`, `gpu`, and `device`. As a disclaimer, no special characters are 
allowed while naming these parameters. Specifically no dashes (`-`) are allowed
either. These can be replaced with underscores (`_`) or periods (`.`).

Setting the `user` and `host` parameters is relatively easy. Make sure you're
in the `mnist` in `reu2022`. To set the `user` parameter, type in the following:

```bash
$ cms set user='user'
```

`'user'` can be what you want to call yourself as long it doesn't reveal your 
real identity. You can use your first name, a nickname, a random keyword, etc.
For example:

```bash
$ cms set user='alex'
```

To set the `host` parameter, type in the following:

```bash
$ cms set host='host'
```

`'host'` is used to specify what type on device you're using. You can specify 
whether you're using a laptop or desktop and what operating system you're
running on. For example: 

```bash
$ cms set host='win11_laptop'
```

## Setting the `cpu` and `gpu` parameters

When you run these `mnist` jobs, you'll be using either your CPU or GPU to run
them. However, you'll have to input these parameters, you'll need to know what 
model you CPU or GPU is. This can be done with the following command:

```bash
$ python getinfo.py
```

The following output is produced on this specific device:

```
CPU: 11th Gen Intel(R) Core(TM) i7-1165G7 @ 2.80GHz
GPU: none
```

After you receive these results, you want to shorten your CPU/GPU names to a
single term with no spaces, dashes, nor special characters. In this case, the
CPU name will be shortened to `i7_1165G7`.

If your device doesn't have a GPU, set device to `'cpu'` with the command:

```bash
$ cms set device='cpu'
```

If your device does have a GPU, set device to `'gpu'` with the command:

```bash
$ cms set device='gpu'
```

## Running the `mnist` Files

In the `mnist` folder located in the `reu2022` folder, there are various 
`mnist` files that can be run. Each test comes in three file formats, which are
in `.ipynb`, `py`, and `.sh` files. On Rivanna, you want to run the `.sh`. The 
following example will run `mlp_mnist.sh`.

```bash
rivanna $ sbatch mlp_mnist.sh
```

This will submit a Slurm job to run the `.sh` file and which will be put in the 
queue that can be viewed using the following command:

```bash
rivanna $ squeue -u $USER
```


