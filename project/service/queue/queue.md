# Queue Data Structure

The queue data structure is a data structure that was built for cloudmesh, a cloud computing platform around which this documentation is based. The queue module is not a queue like the built-in python module. The built-in python module lines up the data in the correct order and implements the push and pop methods correctly. 

The queue structure in the cloudmesh GitHub is a data structure that creates jobs, lines up the jobs in a queue, then places that queue into a larger queues data structure. This makes it so that a user could add jobs to a queue, then add that queue to a list of queues and then run those queues.

This module was built with the intent of allowing researchers to run jobs (with are their experimental tests) on multiple devices and report those jobs back. 

## Location

The code for this project is located on [GitHub](https://github.com/cloudmesh/cloudmesh-cc/blob/main/cloudmesh/cc/queue.py). Please feel free to clone and download and use for your own purposes. 

## Installation

To install this module, simply download the GitHub repository and utilize the correct import statement that you need in order to make this work in the directory you are working in. 

## Contents

In the queue module there are three different classes. 

### `Job`

The `Job` class is an object that creates the job. There are a few things that the objects holds. 

Fields:

It has the fields: name, user, label, command, status, output, output_file, error_file, error, kind, progress, created, and modified. Each of these fields represents necessary information about the job, especially the command. If there is a `.sh` file that you would like to run as opposed to a single command, the command could be to run that `.sh` file!

Methods:

In the `job` module, there are a few methods to assist in leveraging the power of the queue. These methods are: `str`, `dict`, `set`, `update`, `run`, and `get_progress`. The implementations of these methods can be found on [GitHub](https://github.com/cloudmesh/cloudmesh-cc/blob/main/cloudmesh/cc/queue.py). Please review to understand how to utilize these for your program!

### `Queue`

The `Queue` class is a class that allows users to add jobs and then puts those jobs into a dictionary structure with the name of the job followed by the job itself. 

### `Queues`


