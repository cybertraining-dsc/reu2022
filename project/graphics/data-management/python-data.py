import random
import pandas as pd
from matplotlib import pyplot as plt
from cloudmesh.common.util import path_expand

"""

Purpose: python uses several different data structures. It is
         important to know how to operate these data structures.  The
         following is used to demonstrate how the structures work and
         how to use them to create the necessary visuals for data
         analysis.

This code is available on GitHub at the following address:
https://github.com/cybertraining-dsc/reu2022/tree/main/project/graphics/data-management

"""

# Lists

# CSV Files

# Python CSV Module

filename = path_expand("./biostats.csv")
print(filename)

names = []
sex_data = []
age_data = []
height_data = []
weight_data = []


import sys
import csv
from pprint import pprint

with open(filename,'r') as file:  # opens the csv and creates the reader object for it
    table = list(csv.reader(file, delimiter=','))



pprint(table)
'''for line in table[1:]:
    names.append(line[0])
    sex_data.append(line[1])
    age_data.append(line[2])
    height_data.append(line[3])
    weight_data.append(line[4])'''

pprint(table)
# d = table[0]
# def csv_read_to_list(table):
d = {'Names': [],
     'Sex': [],
     'Age': [],
     'Height': [],
     'Weight': []}
for line in table[1:]:
    d['Names'].append(line[0])
    d['Sex'].append(line[1])
    d['Age'].append(line[2])
    d['Height'].append(line[3])
    d['Weight'].append(line[4])

pprint(d)
# d = table[0]

# def csv_read_to_dict(table):
column_names = table[0]
d = {}
for column in table[0]:
    d[column] = []

for line in table[1:]:
    counter = 0
    for column in column_names:
        d[column].append(line[counter])
        counter = counter + 1


sys.exit()

''' for each_row in reader:
        if each_row:  # you have to check for blank lines within the document


with open('/Users/jacksonmiskill/Downloads/biostats.csv',
          'r') as file:
    # opens the csv and creates the reader object for it
    reader = csv.reader(file, delimiter=',')

    for each_row in reader:
        if each_row:
            # you have to check for blank lines within the document

            names.append(each_row[0])
            sex_data.append(each_row[1])
            age_data.append(each_row[2])
            height_data.append(each_row[3])
            weight_data.append(each_row[4])


names.pop(0)
height_data.pop(0)
for i in range(0, len(height_data)):
    height_data[i] = int(height_data[i])
print(type(height_data[0]))
print(height_data)
'''



# let's plot the heights and weight of everyone. We could maybe use a
# hue here to denote who it is
plt.plot(names, height_data)
plt.xlabel("Name")
plt.ylabel("Height")
plt.xticks(rotation=90)
plt.savefig('images/csv-lineplot.png')
plt.savefig('images/csv-lineplot.svg')
plt.savefig('images/pandas-lineplot.pdf')
plt.legend()
plt.title("Names and Corresponding Height")
plt.show()

# Pandas Library

file = pd.read_csv("/Users/jacksonmiskill/Downloads/biostats.csv")
biostats = pd.DataFrame(file)
plt.plot(biostats['Name'], biostats[' "Height (in)"'])
plt.xlabel("Name")
plt.ylabel("Height")
plt.xticks(rotation=90)
plt.savefig('images/pandas-lineplot.png')
plt.savefig('images/pandas-lineplot.svg')
plt.savefig('images/pandas-lineplot.pdf')
plt.title("Names and Corresponding Height")
plt.show()

