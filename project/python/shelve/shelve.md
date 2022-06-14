# Shelve

`shelve` is a library that gives users the ability to create, store, modify, and
control the accessibility of data without a relational database.

## Creating a New Shelf

A new shelf can be created using the command: `shelve.open(filename)`.
`shelve` can store objects and thus you can for example insert a
dictionary as shown next:

```python
import shelve

with shelve.open('computers.db') as computers:
    computers['temperature'] = {
        'red': 80,
        'blue': 40,
        'yellow': 50,
    }
```

## Accessing a Shelf

After it's been created, it can be accessed while readin objects into variables 

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

The user can also make their data read-only by adding the `flag` parameter 
as shown:

```
shelve.open('computers.db', flag='r')
```

That way, when a user tries to modify it, it produces an error:

```python
import dbm
import shelve

with shelve.open('computers.db', flag='r') as computers:
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

## Modifying Shelves with Writeback

In order to modify a shelf, use the parameter `writeback=True` as shown:

```
shelve.open('shelf_name', writeback=True)
```

Make sure to use this before making the modification, or else it won't work.


```python
import shelve
from pprint import pprint

with shelve.open('computers.db', writeback=True) as computers:
    print('Initial temperature:')
    pprint(computers['temperature'])

    computers['temperature']['green'] = 101
    print()
    print('Modified temperature:')
    pprint(computers['temperature'])

```

Modifications are preserved as shown in this output:

```
Initial temperature:
{'red': 80, 'blue': 40, 'yellow': 50}

Modified temperature:
{'red': 80, 'blue': 40, 'yellow': 50, 'green': 101}

```

## Links

* <https://pymotw.com/3/shelve/index.html>


