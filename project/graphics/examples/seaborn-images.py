import seaborn as sns
import matplotlib.pyplot as plt

# creating unique data that can be used for the documentation
# the data represents different a user Spotify Liked Songs break down
data = {'Rock': 136, 'Rap': 112, 'Folk': 110, 'Indie': 90, 'Jazz': 25}
categories = list(data.keys())
count = list(data.values())
personal_rank = [3, 4, 2, 1, 5]

#  Relational Plot- line plot
'''
sns.relplot(x=categories, y=count)
plt.xlabel("Month of the year")
plt.ylabel("Amount of photos taken")
plt.savefig('images/seaborn-lineplot.png')
plt.savefig('images/seaborn-lineplot.svg')
plt.savefig('images/seaborn-lineplot.pdf')
plt.show()
'''
# Distribution Plot -
'''
sns.displot(x=categories, y=count)
plt.savefig('images/seaborn-displot.png')
plt.savefig('images/seaborn-displot.svg')
plt.savefig('images/seaborn-displot.pdf')
plt.show()
'''
# Categorical Plot
'''
sns.barplot(x=categories, y=count)
plt.savefig('images/seaborn-catplot.png')
plt.savefig('images/seaborn-catplot.svg')
plt.savefig('images/seaborn-catplot.pdf')
plt.show()'''

# Regression Plot

sns.regplot(x=personal_rank, y=count)
plt.savefig('images/seaborn-regplot.png')
plt.savefig('images/seaborn-regplot.svg')
plt.savefig('images/seaborn-regplot.pdf')
plt.show()

'''
source = ['Spotify', 'System Services', 'Uninstalled Apps', 'FaceTime', 'Instagram', 'Safari',
          'Maps', 'Gmail', 'Photos', 'GroupMe', 'Podcasts']

value = [19.1, 10.9, 7.4, 4.3, 4.1, 3.9, 3.0, 1.8, 1.6, 1.3, 1.0]
use = ['Yes', 'No', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']

# creating a different set of data that reflects how many photos a user took in each month of 2022 up to June

months = [1, 2, 3, 4, 5]
photos = [91, 151, 138, 101, 49]

# You can also use the seaborn built in data to practice creating the visualizations. 

data = sns.load_dataset("mpg")
sns.set_theme()


dependent_1 = data.horsepower
dependent_2 = data.mpg

independent_1 = data.displacement
independent_2 = data.weight
independent_3 = data.acceleration

hue_1 = data.origin
hue_2 = data.model_year
'''
