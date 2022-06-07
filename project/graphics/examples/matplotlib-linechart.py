import matplotlib.pyplot as plt
import random

x = []
y = []
for i in range(0, 100):
    x.append(i)
    value = random.random() * 100
    y.append(value)

# creating the plot and labeling axes and title
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Plot Test")
plt.savefig('images/matplotlib-linechart.png', dpi=300)
plt.savefig('images/matplotlib-linechart.pdf')
plt.savefig('images/matplotlib-linechart.svg')
plt.show()