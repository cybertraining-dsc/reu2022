import random

"""
Purpose: python uses several different data structures. It is important to know how to operate these data structures.
         The following is used to demonstrate how the structures work and how to use them to create the necessary
         visuals for data analysis.

This code is available on GitHub at the following address: https://github.com/cybertraining-dsc/reu2022/tree/main/project/graphics/data-management

"""

# Lists

x = []
y = []
for i in range(0, 100):
    x.append(i)
    value = random.random() * 10000
    y.append(value)

# to access values of a list

for each in x:
    print(x[i])


