from bokeh.io import show, export_png, export_svg
from bokeh.plotting import figure
from matplotlib import pyplot as plt

import random
import os


def save(p):
    name = os.path.basename(__file__).replace(".py", "")
    plt.savefig(f'images/{name}.png')
    plt.savefig(f'images/{name}.pdf')
    plt.savefig(f'images/{name}.svg')
    show(p)


x = []
y = []
for i in range(0, 100):
    x.append(i)
    value = random.random() * 100
    y.append(value)

p = figure(title="Plot Test", x_axis_label="x", y_axis_label="y")
p.line(x, y)

save(p)
