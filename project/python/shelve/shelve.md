# Shelve

`shelve` is a library that gives users the ability to create, store,
modify, and control the accessibility of data without a relational
database. A shelf has a string key and data that can be near anything
as long as it is supported by `pickle`. This includes integers,
dictionaries, and Objects.

## Creating a New Shelf

A new shelf can be created using the command: `d =
shelve.open(filename)`.  Shelve can store objects; you can insert a
dictionary, for example, as shown next:

```python
import shelve

computers = shelve.open('computers.db')
computers['temperature'] = {
    'red': 80,
    'blue': 40,
    'yellow': 50,
}
```

*On a Windows:*
This creates three files `computers.db.bak`, `computers.db.dat`, and
`computers.db.dir`. These `.bak`, `.dat`, and `.dir` files hold the
shelf information that can be accessed for future use.

For other computers, this creates the file 'computers.db'.

## Accessing a Shelf

After it's been created, it can be accessed while reading objects into
variables.

```python
import shelve

with shelve.open('computers.db') as computers:
    t = computers['temperature']

print(t)
```

This produces the following output:

```
{'red': 80, 'blue': 40, 'yellow': 50}
```

## Making Shelf Read-Only

The user can also make their data read-only by adding the `flag`
parameter as shown:

```
shelve.open('computers.db', flag='r')
```

That way, when a user tries to modify it, it produces an error:

```python
import dbm
import shelve

computers = shelve.open('computers.db', flag='r')
print('Temperature:', computers['temperature'])
try:
    computers['temperature']['green'] = 100
except dbm.error as err:
    print('ERROR:', err)
```

The following output is produced:

```
Temperature: {'red': 80, 'blue': 40, 'yellow': 50}
ERROR: The database is opened for reading only
```

## Modifying Shelves

In order to modify a shelf, simply open up the shelf again as shown:

```
shelve.open('shelf_name')
```

Make sure to use this before making the modification, or else it won't
work.  For simple assignments, this will suffice.

However, in most cases, you use the `writeback=True` parameter. This
caches the modifications and slows down the saving process. As seen,
however, you can now directly access and modify the shelf entries as
it was a two-dimensional dictionary.

You can also delete shelf items using their keys with the `del`
method.

```python
import shelve
from pprint import pprint

computers = shelve.open("computers.db",writeback=True)
print('Initial temperature:')
pprint(computers['temperature'])

computers['temperature']['green'] = 101
del computers['temperature']['yellow']
print()
print('Modified temperature:')
pprint(computers['temperature'])
```

Modifications are preserved as shown in this output:

```
Initial temperature:
{'red': 80, 'blue': 40, 'yellow': 50}

Modified temperature:
{'blue': 40, 'green': 101, 'red': 80}
```

## Closing Shelves

Lastly, in order to save the shelf so that it may be accessed next
time, use the command '.close()'

```python
import shelve

computers = shelve.open('computers.db')
# do your shelf operations here
computers.close()
```

## Links

* [Shelve Documentation](https://pymotw.com/3/shelve/index.html)
* [Python Object Persistence](https://docs.python.org/3/library/shelve.html>)
