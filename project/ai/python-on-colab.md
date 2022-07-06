# Python On Colab

Python Exercise on Google Colab

## Python Exercise on Google Colab


* [Open In Colab](https://colab.research.google.com/github/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/python_warmup.ipynb)   
* [View in Github](https://github.com/cybertraining-dsc/cybertraining-dsc.github.io/blob/master/content/en/modules/notebooks/python_warmup.ipynb)   
* [Download](https://raw.githubusercontent.com/cybertraining-dsc/cybertraining-dsc.github.io/master/content/en/modules/notebooks/python_warmup.ipynb)


In this exercise, we will take a look at some basic Python Concepts
needed for day-to-day coding.

* Youtube Video: <http://youtube.com/watch?v=x1ICvWDlvB0>

Check the installed Python version.


```
! python --version    
```
Python 3.7.6

## Simple For Loop


```
for i in range(10):
  print(i)
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9

## List


```
list_items = ['a', 'b', 'c', 'd', 'e']
```

### Retrieving an Element


```
list_items[2]
```

    'c'

### Append New Values


```
list_items.append('f')
list_items
```

    ['a', 'b', 'c', 'd', 'e', 'f']

### Remove an Element


```
list_items.remove('a')
list_items
```

    ['b', 'c', 'd', 'e', 'f']

* Youtube Video: <http://youtube.com/watch?v=oudT4sRIuwU>

## Dictionary


```
dictionary_items = {'a':1, 'b': 2, 'c': 3}
```

### Retrieving an Item by Key


```
dictionary_items['b']
```

    2

### Append New Item with Key


```
dictionary_items['c'] = 4
dictionary_items
```

    {'a': 1, 'b': 2, 'c': 4}

### Delete an Item with Key


```
del dictionary_items['a'] 
dictionary_items
```

    {'b': 2, 'c': 4}

## Comparators


```
x = 10
y = 20 
z = 30
x > y 
```

    False


```
x < z
```

    True


```
z == x
```

    False


```
if x < z:
  print("This is True")
```

    This is True


```
if x > z:
  print("This is True")
else:
  print("This is False")  
```

    This is False

* Youtube Video: <http://youtube.com/watch?v=GKU6-SNZGQc>

## Arithmetic


```
k = x * y * z
k
```

    6000


```
j = x + y + z
j
```

    60


```
m = x -y 
m
```

    -10


```
n = x / z
n
```

    0.3333333333333333

## Numpy

### Create a Random Numpy Array


```
import numpy as np
a = np.random.rand(100)
a.shape
```

    (100,)

### Reshape Numpy Array


```
b = a.reshape(10,10)
b.shape
```

    (10, 10)

### Manipulate Array Elements

```
c = b * 10
c[0]
```

    array([3.33575458, 7.39029235, 5.54086921, 9.88592471, 4.9246252 ,
           1.76107178, 3.5817523 , 3.74828708, 3.57490794, 6.55752319])


```
c = np.mean(b,axis=1)
c.shape
```

    10


```
print(c)
```

    [0.60673061 0.4223565  0.42687517 0.6260857  0.60814217 0.66445627 
      0.54888432 0.68262262 0.42523459 0.61504903]

