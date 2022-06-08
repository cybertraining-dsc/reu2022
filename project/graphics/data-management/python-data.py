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



# let's plot the heights and weight of everyone. We could maybe use a hue here to denote who it is
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

