import matplotlib.pyplot as plt

data = {'Rock': 136, 'Rap': 112, 'Folk': 110, 'Indie': 90, 'Jazz': 25}
categories = data.keys()
count = data.values()

# Creating the pie chart
plt.pie(count, labels=categories)

plt.savefig('images/matplotlib-piechart.png', dpi=300)
plt.savefig('images/matplotlib-piechart.pdf')
plt.savefig('images/matplotlib-piechart.svg')
plt.show()
