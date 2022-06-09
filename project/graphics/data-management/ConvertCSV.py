"""
Purpose: python uses several different data structures. It is important to know how to operate these data structures.
         The following is used to demonstrate how the structures work and how to use them to create the necessary
         visuals for data analysis.

This code is available on GitHub at the following address: https://github.com/cybertraining-dsc/reu2022/tree/main/project/graphics/data-management

"""

import random
import pandas as pd
from matplotlib import pyplot as plt
import csv
from cloudmesh.common.util import path_expand
import sys

class ConvertCSV:

    table = []
    variables = 0

    def create_table(self, num_params):
        filename = path_expand(f"{self}.csv")
        with open(filename, 'r') as file:  # opens the csv and creates the reader object for it
            table = list(csv.reader(self, delimiter=','))
            variables = num_params
        return table

    def csv_read_to_list(self):

    def csv_read_to_dict(self):





