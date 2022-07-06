# Databases Program

The database program is a selection of different implmentations that allow a user to save objects and variables in specific files through which they can access these files and utilize them for the proper use cases. 

There are two different database examples that have been created: yamldb and shelve.

## Location

These programs are located in cloudmesh-cc, which is available on [GitHub](https://github.com/cloudmesh/cloudmesh-cc/tree/main/cloudmesh/cc/db). You can download and utilize these programs to your liking. 

## Contents

Inside each of the database programs are many functions that make it easy for a user to utilize the program to their needs. 

In yamldb:  `__init__`, `save`, `load`, `remove`, `get`, `get_queue`, `get_job`, `__setitem__`, `__str__`, `clear`, `queues`, and `info`. 

In shelve: `__init__`, `queues`, `filename`, `shelvename`, `info`, `load`, `save`, `close`, `remove`,`get`, `getitem`, `set`, `__setitem__`, `__str__`, `delete`, `__delitem__`, `clear`, and `len`


## Initialization

The typical use case for these databases is to add it to another object class so that that class can be saved to a database and accessed for testing and for scripting implementation. 

In order to do so, the database should be introduced in the initialization of the object:

```python
class Queues:
    def __init__(self, filename=None):
        """
        Initializes the queue structure.
        """

        if filename is None:
            filename = "~/.cloudmesh/queue/queue.yamldb"

        self.db = QueueDB(filename=filename)
        self.counter = 0
```

This code can be access on [GitHub](https://github.com/cloudmesh/cloudmesh-cc/blob/main/cloudmesh/cc/queue.py)

So now the database can be called from within the object as well as outside the object (i.e. in other programs where a `Queues` object has been created)!. 