# Shelve Summary

Shelve is a library that gives users the ability to create, store, modify, and
control the accessibility of data without a relational database.

## Import Statement

This should be the very first line a user must write before proceeding:

```python
import shelve
```

## Creating a New Shelf

A new shelf can be created using the command: `shelve.open('shelf_name')`. 
User data can be inputted in the lines below as shown in this [example](https://github.com/cybertraining-dsc/reu2022/blob/main/project/examples/shelve_instructions/shelve_create.py) where
it's in the form of a dictionary:

```python
import shelve

with shelve.open('fav_color.db') as s:
    s['votes'] = {
        'red': 5,
        'blue': 3,
        'yellow': 2,
    }
```

## Accessing a Shelf

After it's been created, it can be accessed as shown [here](https://github.com/cybertraining-dsc/reu2022/blob/main/project/examples/shelve_instructions/shelve_existing.py):
```python
with shelve.open('fav_color.db') as s:
    existing = s['votes']

print(existing)
```

This produces the following output:

`{'red': 5, 'blue': 3, 'yellow': 2}`

## Making Shelf Read-Only

The user can also make their data read-only by adding the `flag` parameter 
as shown:

`shelve.open('shelf_name', flag='r')`

That way, when a user tries to modify it, it produces an error, as shown in this
[example](https://github.com/cybertraining-dsc/reu2022/blob/main/project/examples/shelve_instructions/shelve_readonly.py):

```python
import dbm
import shelve

with shelve.open('fav_color.db', flag='r') as s:
    print('Existing:', s['votes'])
    try:
        s['votes'] = 'green'
    except dbm.error as err:
        print('ERROR: {}'.format(err))
```

The following output is produced:

`Existing: {'red': 5, 'blue': 3, 'yellow': 2} 
ERROR: The database is opened for reading only`

## Modifying Shelves with Writeback

In order to modify a shelf, use the parameter `writeback=True` as shown:

`shelve.open('shelf_name', writeback=True)`

Make sure to use this before making the modification, or else it won't work.

Here is an [example](https://github.com/cybertraining-dsc/reu2022/blob/main/project/examples/shelve_instructions/shelve_writeback.py)
of how it can be modified:

```python
import shelve
import pprint

with shelve.open('fav_color.db', writeback=True) as s:
    print('Initial data:')
    pprint.pprint(s['votes'])

    s['votes']['green'] = 5
    print('\nModified:')
    pprint.pprint(s['votes'])

with shelve.open('fav_color.db', writeback=True) as s:
    print('\nPreserved:')
    pprint.pprint(s['votes'])
```

Modifications are preserved as shown in this output:

```
Initial data:
{'blue': 3, 'red': 5, 'yellow': 2}`

Modified:
{'blue': 3, 'green': 5, 'red': 5, 'yellow': 2}

Preserved:
{'blue': 3, 'green': 5, 'red': 5, 'yellow': 2}
```



