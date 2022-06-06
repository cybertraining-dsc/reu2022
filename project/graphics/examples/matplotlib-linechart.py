import matplotlib.pyplot as plt
import random

x = []
for i in range(0, 100):
    value = random.random() * 10000
    x.append(value)

# creating a list of 100 numbers in order from 0 to 100
y = []
for j in range(0, 100):
    y.append(j)

# creating the plot and labeling axes and title
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Plot Test")
plt.savefig('images/matplotlib-linechart.png', dpi=300)
plt.savefig('images/matplotlib-linechart.pdf')
plt.savefig('images/matplotlib-linechart.svg')
plt.show()