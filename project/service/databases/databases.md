# Databases Program

The database program is a selection of different implementations that allow a user to save objects and variables in specific files through which they can access these files and utilize them for the proper use cases. 

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
from cloudmesh.cc.db.yamldb.database import Database as QueueDB
# from cloudmesh.cc.db.shelve.database import Database as QueueDB

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

## Usage

It is super simple to use the databases. They are implemented in a way so as to maximize user ease and capability. First of all, it is necessary to use the above methods for each of the two databases that were implemented. These methods allow for ease of access. In the `Queues` class that was implemented, there are a few methods that draw upon this database. We will explore them. 

```python
    def save(self):
        """
        save the queue to persistent storage
        """
        self.db.save()

    def load(self):
        self.db.load()
```

This code can be accessed on [GitHub](https://github.com/cloudmesh/cloudmesh-cc/blob/main/cloudmesh/cc/queue.py).

As you can see, the save and load methods have been implemented. After the instantiation of the database in the previous code block, the user can call the database using `self.db` to access it. Loading the database simply pulls the data from the file and loads it in a dictionary-like format. Saving the database allows you to push changes that you have made back into the database. 

```python
    def info(self):
        return self.db.info()
```

This code can be accessed on [GitHub](https://github.com/cloudmesh/cloudmesh-cc/blob/main/cloudmesh/cc/queue.py).

This command simply accessed the information provided by the database (ie. what is being stored in the database).

```python
@property
    def queues(self):
        return self.db.queues

    @property
    def config(self):
        return self.db.data['config']
```

This code can be accessed on [GitHub](https://github.com/cloudmesh/cloudmesh-cc/blob/main/cloudmesh/cc/queue.py).

This code showcases a special way that the database can be used. In this queues class, we have a way to access specific objects that we have stored into the database. In the database, we have set a characteristic to be `queues`, which holds a dictionary of queue names to queues of jobs. In creating this special method, we allow programmers to very quickly and easily grab the queues that they need. This could be extrapolated, too. There could be another method that looks for only a `queue`. It could be implemented like so:

```python
    def queue(self, name):
        """
        return the whole queue that the name in the parameter specifies
        """
        
        queues = self.queues()
        queue = queues[name]
        return queue
```

This code is not accessible anywhere, as it was written as a (untested) pseudo-code specifically for the discussion in this section of the documentation. 

As you can see, this would allow a programmer not only access to the whole queues structure, but it would also allow access to a specific queue!

## Extension

These are not the only types of files that can be used to save data. There could be other modules out there that exist for the purpose of implementation in another fashion. 