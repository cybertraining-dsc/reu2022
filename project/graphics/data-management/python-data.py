import random
import csv
import pandas as pd


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

# Python CSV Module

biostats = open('/Users/jacksonmiskill/Downloads/biostats.csv') # opens the csv and creates the reader object for it
reader = csv.reader(biostats)

age_data = []
for each_row in reader:
    if each_row: # you have to check for blank lines within the document
        age_data.append(each_row[2])

print(age_data)
biostats.close()


# Pandas Library

file = pd.read_csv("/Users/jacksonmiskill/Downloads/biostats.csv")
biostats = pd.DataFrame(file)

print(biostats



