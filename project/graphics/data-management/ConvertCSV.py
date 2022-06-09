"""
Purpose: python uses several different data structures. It is important to know how to operate these data structures.
         The following is used to demonstrate how the structures work and how to use them to create the necessary
         visuals for data analysis.

This code is available on GitHub at the following address: https://github.com/cybertraining-dsc/reu2022/tree/main/project/graphics/data-management

"""


import csv
from cloudmesh.common.util import path_expand


def create_table(filename):
    filename = path_expand(f"{filename}.csv")

    with open(filename, 'r') as file:  # opens the csv and creates the reader object for it
        table = list(csv.reader(file, delimiter=','))
    return table


def csv_read_to_list(table, index):
    column_names = table[0]

    ilist = []
    for first in table[1: ]:
        ilist.append(table[first][index])

    return ilist

def csv_read_to_dict(table, index):

    idict = {}
    counter = 0
    for x in table[1:]:
        idict[table[x]].append(table[x][index])

    return idict
    







