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

df = pd.DataFrame({'Count':count},index=categories)
plot = df.plot.pie(y='Count')
save()