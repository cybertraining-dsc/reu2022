import matplotlib.pyplot as plt
import pandas as pd
import random
import os

def save ():
    name = os.path.basename(__file__).replace(".py", "")
    plt.savefig(f"images/{name}.png", dpi=300)
    plt.savefig(f"images/{name}.pdf")
    plt.savefig(f"images/{name}.svg")
    plt.show()

x = []
for i in range(0, 100):
    value = random.random() * 10000
    x.append(value)

# creating a list of 100 numbers in order from 0 to 100
y = []
for j in range(0, 100):
    y.append(j)

df = pd.DataFrame({'x':x, 'y':y})
print(df.head())

# creating the plot and labeling axes and title
df.plot.line(x='x', y='y')
# plt.xlabel("x")
plt.ylabel("y")
plt.title("Plot Test")

save()
