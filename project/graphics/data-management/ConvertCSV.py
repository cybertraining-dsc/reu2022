"""
    Purpose: to access the csv module and utilize it to create lists and dictionaries

    Author: Jackson Miskill
    Contact: jcm4bsq@virginia.edu
"""

import csv
from cloudmesh.common.util import path_expand


def create_table(filename):
    filename = path_expand(f"{filename}.csv")

    with open(filename, 'r') as file:  # opens the csv and creates the reader object for it
        table = list(csv.reader(file, delimiter=','))
    return table


def csv_read_to_list(table, index):
    ilist = []
    for first in range(1, len(table)):
        ilist.append(table[first][index])

    return ilist


def csv_read_to_dict(table, index):
    idict = {}

    for value in range(1, len(table)):
        idict[table[value][0]] = int(table[value][index])

    return idict
