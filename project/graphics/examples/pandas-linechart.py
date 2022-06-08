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
y = []
for i in range(0, 100):
    x.append(i)
    value = random.random() * 100
    y.append(value)

df = pd.DataFrame({'x':x, 'y':y})

# creating the plot and labeling axes and title
df.plot.line(x='x', y='y')
# plt.xlabel("x")
plt.ylabel("y")
plt.title("Plot Test")

save()
