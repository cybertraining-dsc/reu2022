# Pickle Summary

Pickle is a module that turns Python objects into series of bytes that can be 
transmitted, stored, or reconstructed.

## Import Statement

This should be the very first line a user must write before proceeding:

```python
import pickle 
```

## Encoding Data

A data structure can be encoded into a string by using the command 
`pickle.dumps(data)`. In this [example], a dictionary is being encoded. 

```python
import pickle

# Creating dictionary of data
votes = [{'Red': 5, 'Blue': 3, 'Yellow': 2}]
print('Votes:', votes)

# Pickling the data
pickle_votes = pickle.dumps(votes)
print('Pickle:', pickle_votes)
```

This following output is produced:
```
Votes: [{'Red': 5, 'Blue': 3, 'Yellow': 2}]
Pickle: b'\x80\x04\x95$\x00\x00\x00\x00\x00\x00\x00]\x94}\x94(\x8c\x03Red\x94K\x05\x8c\x04Blue\x94K\x03\x8c\x06Yellow\x94K\x02ua.'
```

## Decoding Data

The encoded data can then be decoded using the command `pickle.loads(data)`.

```python
import pickle

# Creating dictionary of data
votes1 = [{'Red': 5, 'Blue': 3, 'Yellow': 2}]
print('Before:', votes1)

# Encoding the data
pickle_votes = pickle.dumps(votes1)

# Decoding the data
votes2 = pickle.loads(pickle_votes)
print('After:', votes2)

# Checking authenticity
print('Same:', (votes1 is votes2))
print('Equal:', (votes1 == votes2))
```

This can be shown in the following output:
```
Before: [{'Red': 5, 'Blue': 3, 'Yellow': 2}]
After: [{'Red': 5, 'Blue': 3, 'Yellow': 2}]
```

This command will produce data that is equal to the original data, but it's not
the same as shown by the following output:

```
Same: False
Equal: True
```

## Streaming
