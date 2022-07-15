#!/usr/bin/env python
# coding: utf-8

# ## Python Warm Up
# 
# In this exercise, we will take a look at some basic Python Concepts needed for
# day-to-day coding. 

# Check the installed Python version.



# get_ipython().system(' python --version')


# ## Simple For Loop



for i in range(10):
  print(i)


# ## List



list_items = ['a', 'b', 'c', 'd', 'e']


# ### Retrieving an Element



list_items[2]


# ### Append New Values



list_items.append('f')




list_items


# ### Remove an Element



list_items.remove('a')




list_items


# ## Dictionary



dictionary_items = {'a':1, 'b': 2, 'c': 3}


# ### Retrieving an Item by Key



dictionary_items['b']


# ### Append New Item with Key



dictionary_items['d'] = 5




dictionary_items


# ### Delete an Item with Key



del dictionary_items['a'] 




dictionary_items







# ## Comparators



x = 10
y = 20 
z = 30




x > y 




x < z




z == x




if x < z:
  print("This is True")




if x > z:
  print("This is True")
else:
  print("This is False")  


# ## Arithmetic



k = x * y * z
k




j = x + y + z
j




m = x -y 
m


# 



n = x / z
n


# ## Numpy

# ### Create a Random Numpy Array 



import numpy as np




a = np.random.rand(100)
a.shape


# ### Reshape Numpy Array



b = a.reshape(10,10)
b.shape


# ### Manipulate Array Elements



c = b * 10
c[1][0]




c = np.mean(b,axis=1)
c.shape




print(c)






