# importing both seaborn and matplotlib

import seaborn as sns
import matplotlib.pyplot as plt
import random


# Load the miles per gallon dataset

data = sns.load_dataset("mpg")
sns.set_theme()

dependent_1 = data.horsepower
dependent_2 = data.mpg

independent_1 = data.displacement
independent_2 = data.weight
independent_3 = data.acceleration

hue_1 = data.origin
hue_2 = data.model_year

#  Relational Plot- line plot

'''
sns.lineplot( x=independent_1 , y=dependent_1, hue=hue_1)
plt.savefig('images/seaborn-lineplot.png')
plt.savefig('images/seaborn-lineplot.svg')
plt.savefig('images/seaborn-lineplot.pdf')
plt.show()
'''
# Distribution Plot -

'''
sns.displot(x=independent_2, y=dependent_2, hue=hue_1)
plt.savefig('images/seaborn-displot.png')
plt.savefig('images/seaborn-displot.svg')
plt.savefig('images/seaborn-displot.pdf')
plt.show()
'''

# Categorical Plot

"""
sns.catplot(x="displacement", data=data, kind="count")
plt.savefig('images/seaborn-catplot.png')
plt.savefig('images/seaborn-catplot.svg')
plt.savefig('images/seaborn-catplot.pdf')
plt.show()
"""


# Regression Plot

sns.regplot(x=independent_1, y=dependent_1)
plt.savefig('images/seaborn-regplot.png')
plt.savefig('images/seaborn-regplot.svg')
plt.savefig('images/seaborn-regplot.pdf')
plt.show()
