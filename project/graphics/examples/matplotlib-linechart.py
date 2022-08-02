import matplotlib.pyplot as plt
import random

def save_plt(name):
  plt.savefig(f'{name}.png', dpi=300)
  plt.savefig(f'{name}.pdf')
  plt.savefig(f'{name}.svg')
  plt.show()

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

save_plt("images/matplotlib-linechart")
