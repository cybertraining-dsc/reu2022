import matplotlib.pyplot as plt
import pandas as pd
import sys

# you can also do this: from matplotlib import pyplot as plt

data = {'Rock': 136, 'Rap': 112, 'Folk': 110, 'Indie': 90, 'Jazz': 25}
categories = data.keys()
count = data.values()

df = pd.DataFrame(data=(categories, count))
df = df.transpose()

df.columns = ["Categories","Count"]
df.set_index("Categories")

print(df.head())

# Creating the bar chart
df.plot.bar(
        align='center',
        color='orange',
        width=0.9,
        edgecolor="black",
        linewidth=2)

# Editing the bar chart's title, x, and y axes
plt.xlabel("Genre of Music")
plt.ylabel("Number of songs in the genre")
plt.title("Distribution of Genres in My Liked Songs")
plt.show()
