import matplotlib.pyplot as plt
import pandas as pd
import os


def save():
    name = os.path.basename(__file__).replace(".py", "")
    plt.savefig(f"images/{name}.png", dpi=300)
    plt.savefig(f"images/{name}.pdf")
    plt.savefig(f"images/{name}.svg")
    plt.show()


data = {'Rock': 136, 'Rap': 112, 'Folk': 110, 'Indie': 90, 'Jazz': 25}
categories = data.keys()
count = data.values()

df = pd.DataFrame({'Count':count, 'Categories':categories})

# Creating the bar chart
df.plot.bar(
        x='Categories',
        y='Count',
        align='center',
        color='orange',
        width=0.9,
        edgecolor="black",
        linewidth=2)

# Editing the bar chart's title, x, and y axes
plt.xlabel("Genre of Music")
plt.ylabel("Number of songs in the genre")
plt.title("Distribution of Genres in My Liked Songs")

save()
