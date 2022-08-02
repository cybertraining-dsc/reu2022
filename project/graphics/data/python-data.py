import ConvertCSV
from cloudmesh.common.util import path_expand
from matplotlib import pyplot as plt
import pandas as pd


"""

Purpose: python uses several different data structures. It is
         important to know how to operate these data structures.  The
         following is used to demonstrate how the structures work and
         how to use them to create the necessary visuals for data
         analysis.

This code is available on GitHub at the following address:
https://github.com/cybertraining-dsc/reu2022/tree/main/project/graphics/data-management

"""
# reading in the data!
filename = path_expand("./biostats")
table = ConvertCSV.create_table(filename)
print(table)

list_names = []
list_heights = []


list_names = ConvertCSV.csv_read_to_list(table=table, index=0, convert=False)
list_heights = ConvertCSV.csv_read_to_list(table=table, index=3, convert=True)

dict_names = []
dict_heights = []

idict = ConvertCSV.csv_read_to_dict(table=table, index=3)
dict_names = list(idict.keys())
dict_heights = list(idict.values())

# now just plot these values. You can use whichever library you desire
# for the example, we use matplotlib, because it is simple

# list
plt.plot(list_names, list_heights)
plt.xlabel("Names")
plt.ylabel("Heights")
plt.xticks(rotation=90)
plt.savefig('images/csv-list-lineplot.png')
plt.savefig('images/csv-list-lineplot.svg')
plt.savefig('images/csv-list-lineplot.pdf')
plt.title("Names and Corresponding Height")
plt.show()

# dictionary
plt.plot(dict_names, dict_heights)
plt.xlabel("Names")
plt.ylabel("Heights")
plt.xticks(rotation=90)
plt.savefig('images/csv-dict-lineplot.png')
plt.savefig('images/csv-dict-lineplot.svg')
plt.savefig('images/csv-dict-lineplot.pdf')
plt.title("Names and Corresponding Height")
plt.show()

# Now to use pandas, which is significantly easier

file = pd.read_csv('/Users/jacksonmiskill/cm/reu2022/project/graphics/data-management/biostats.csv')
biostats = pd.DataFrame(file)
plt.plot(biostats['Name'], biostats[' "Height (in)"'])
plt.xlabel("Names")
plt.ylabel("Heights")
plt.xticks(rotation=90)
plt.savefig('images/pandas-lineplot.png')
plt.savefig('images/pandas-lineplot.svg')
plt.savefig('images/pandas-lineplot.pdf')
plt.title("Names and Corresponding Height")
plt.show()
