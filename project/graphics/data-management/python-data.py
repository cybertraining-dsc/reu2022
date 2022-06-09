import ConvertCSV
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
filename = path_expand("./biostats")
print(filename)

names = []
sex_data = []
age_data = []
height_data = []
weight_data = []

table = ConvertCSV.create_table(filename)
print(table)

sex_data = ConvertCSV.csv_read_to_list(table=table, index=1)
print(sex_data)

idict = ConvertCSV.csv_read_to_dict(table=table, index=3)
print(idict)




