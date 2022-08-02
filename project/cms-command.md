# cms sys command generate

---

![](images/learning.png) **Learning Objectives**

* Learn how to create your own cloudmesh commands

---

Assignment:

Locate in the book how to use cms sys command generate. Generate a command with your username. No commit of this is necessary, but we need to make 
sure you understand how to create a command.

## Creating CLI commands using the cloudmesh command

Command line interface commands essentially allow a user to execute commands that have been programmed in `python` from the command line (i.e. on a `macOS` terminal). In the `cloudmesh` project, it is easy to do this, as there is a built-in module that allows a user to develop this command. We assume that the user has properly set up cloudmesh on their own device. The following showcases the `sys command generate`:

* Execute `cms sys command generate` in the home directory of the device. This essentially calls a function within cloudmesh cmd5 that allows 
* Once you have done this, it is necessary to `cd` to that directory. For instance, if you typed: `cms sys command generate apples`, then that would have created a command within the directory you were in. Thus, you need to change directory and navigate to that new directory. Then, it is necessary to run `python setup.py` in your command line. Then execute `pip install .`This will configure your device to have the proper requirements for the command that you are generating. 
* After this, you can create python scripts within the directory that can be called as an actual command. You will notice a directory called `cloudmesh` --> `"your command"` --> `command` --> and then finally, `"yourcommand".py`. In this final `python` file, you can edit and create what it is you were intending on creating.
* When you add new arguments to the command, you have to add those arguments to the `arguments parser` function. This ensures that the parser correctly separates all arguments of the program. 
* Finally, in the `if` statements at the end of the program, it is necessary to indicate what arguments/options are specified and what should be done if these commands + arguments + options are called.

**Important Sidebar** 

The generate command function relies on an API base called `docopts` which is a framework for creating a command line interface. What this does in essence is it creates command line commands based on the framework of a python script. 

In this framework there are a few parts to understand:
* Usage- indicate how the commands would be called, specifically. 
* Arguments- indicates what can be passed into the commands to make them work in a specific way. 
* Options- indicates the options that can be specified. These are optional. 

It is necessary to update the arguments in the corresponding if statement. 

### Example of the CLI Creation

Here is an example command:

```python
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
class GregorCommand(PluginCommand):
@command
def do_gregor(self, args, arguments):
"""
::
Usage:
gregor -f FILE
gregor list
This command does some useful things.
Arguments:
FILE a file name
Options:
-f specify the file
"""
print(arguments)
if arguments.FILE:
print("You have used file: ", arguments.FILE)
return ""
```

This example can be found [here](https://cloudmesh-community.github.io/pub/vonLaszewski-python.pdf) in section **6.0.7.1.4 Create your own Extension**. 

Again, all of this relies on having cloudmesh properly downloaded and installed. 

### Example of CLI meshing with a python script


CLI Implementation:

```python
    def do_cc(self, args, arguments):
        """
        ::

          Usage:
                cc upload --data=FILENAME
                cc update --data=FILENAME
                cc delete --data=FILENAME
                cc create --queues=QUEUES --database=DATABASE
                cc add --queue=QUEUE --job=JOB --command=COMMAND
                cc run --queue=QUEUE --scheduler=SCHEDULER
                cc remove --queue=QUEUE --job=JOB
                cc remove --queue=QUEUE
                cc list --queue=QUEUE
                cc start
                cc stop
                cc doc
                cc test
                cc temperature

. . .
```

This code can be found [here](https://github.com/cloudmesh/cloudmesh-cc/blob/main/cloudmesh/cc/command/cc.py)

Part of the code implementation of the above CLI:

```python
class Queues:
    """
    The Queues data structure is a structure that holds all of the queues
    with their corresponding names. It is a meta-queue, essentially. The queues
    class will be a dictionary of dictionaries of jobs, which are
    job names and commands.
    An example command would likely look like:
        cms cc queues list --queues=ab
    """

    def __init__(self, database='yamldb'):
        """
        Initializes the giant queue structure.
        Default database is yamldb
        :param name: name of the structure
        :return: creates the queues structure
        """
        if database.lower() == 'yamldb':
            from cloudmesh.cc.db.yamldb.database import Database as QueueDB
            self.filename = path_expand("~/.cloudmesh/queue/queue")

        elif database.lower() == 'shelve':
            from cloudmesh.cc.db.shelve.database import Database as QueueDB
            self.filename = path_expand("~/.cloudmesh/queue/queue")

        else:
            raise ValueError("This database is not supported for Queues, please fix.")
```

This code can be found on [GitHub](https://github.com/cloudmesh/cloudmesh-cc/blob/main/cloudmesh/cc/queue.py)



