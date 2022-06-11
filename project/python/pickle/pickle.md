# Pickle

`pickle` is a module that turns Python objects into series of bytes that can be 
transmitted, stored, or reconstructed.

## Encoding Data

A data structure can be encoded into a string by using the command 
`pickle.dumps(data)`. In this [example](https://github.com/cybertraining-dsc/reu2022/blob/main/project/examples/pickle_instructions/pickle_string.py),
a dictionary is being encoded. 

```python
import pickle

# Creating dictionary of data
temperatures = {
    'red': 50,
    'blue': 30,
    'yellow': 20,
}
print('Temperatures:', temperatures)

# Pickling the data
pickle_temperatures = pickle.dumps(temperatures)
print('Pickle:', pickle_temperatures)
```

This following output is produced:

```
temperatures: [{'Red': 50, 'Blue': 30, 'Yellow': 20}]
Pickle: b' ... A binary string that we ommitted here ... .'
```

## Decoding Data

The encoded data can then be decoded using the command `pickle.loads(data)`:

```python
import pickle

# Creating dictionary of data
temperatures_0 = {'red': 50, 'blue': 30, 'yellow': 20}]
print('Initial temperatures:', temperatures_0)

# Encoding the data
pickle_temperatures_0 = pickle.dumps(temperatures_0)

# Decoding the data
temperatures_1 = pickle.loads(pickle_temperatures_0)
print('From pickle database:', temperatures_1)

# Checking authenticity
print("Same:", temperatures1 is temperatures2)
print("Equal:", temperatures1 == temperatures2)
```

This can be shown in the following output:
```
Initial temperatures: [{'Red': 5, 'Blue': 3, 'Yellow': 2}]
From pickle database: [{'Red': 5, 'Blue': 3, 'Yellow': 2}]
```

This command will produce data that is equal to the original data, but it's not
the same as shown by the following output:

```
Same: False
Equal: True
```

## Links

* <https://pymotw.com/3/pickle/index.html>


