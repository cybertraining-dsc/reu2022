import random
import csv
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

"""
Purpose: python uses several different data structures. It is important to know how to operate these data structures.
         The following is used to demonstrate how the structures work and how to use them to create the necessary
         visuals for data analysis.

This code is available on GitHub at the following address: https://github.com/cybertraining-dsc/reu2022/tree/main/project/graphics/data-management

"""

# Lists

''' x = []
y = []
for i in range(0, 100):
    x.append(i)
    value = random.random() * 10000
    y.append(value)

# to access values of a list



'''

x = []
y = []

with open('/Users/jacksonmiskill/Downloads/biostats.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')

    for row in plots:
        x.append(row[0])
        y.append(int(row[2]))

plt.bar(x, y, color='g', width=0.72, label="Age")
plt.xlabel('Names')
plt.ylabel('Ages')
plt.title('Ages of different persons')
plt.legend()
plt.show()

# CSV Files

# P'''ython CSV Module
names = []
sex_data = []
age_data = []
height_data = []
weight_data = []

with open('/Users/jacksonmiskill/Downloads/biostats.csv',
          'r') as file:  # opens the csv and creates the reader object for it
    reader = csv.reader(file, delimiter=',')

    for each_row in reader:
        if each_row:  # you have to check for blank lines within the document

            names.append(each_row[0])
            if each_row[1] != str:
                sex_data.append(each_row[1])
            if each_row[2] != str:
                age_data.append(each_row[2])
            if each_row[3] != str:
                height_data.append(each_row[3])
            if each_row[4] != str:
                weight_data.append(each_row[4])

print(height_data)
print(weight_data)
'''
# let's plot the heights and weight of everyone. We could maybe use a hue here to denote who it is
plt.plot(names, height_data)
plt.xlabel("Names")
plt.ylabel("Weight")
plt.legend()
plt.title("Corresponding Heights and Names")
plt.show()

# Pandas Library

'''
file = pd.read_csv("/Users/jacksonmiskill/Downloads/biostats.csv")
biostats = pd.DataFrame(file)

print(biostats)

