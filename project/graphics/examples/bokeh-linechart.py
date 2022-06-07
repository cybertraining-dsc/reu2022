from bokeh.io import show, export_png, export_svg
from bokeh.plotting import figure
from selenium import webdriver
import chromedriver_binary
import random
import os

def save (p):
    name = os.path.basename(__file__).replace(".py", "")
    export_png(p, filename=f"images/{name}.png")
    export_svg(p, filename=f"images/{name}.svg")
    show(p)

x = []
for i in range(0, 100):
    value = random.random() * 10000
    x.append(value)

# creating a list of 100 numbers in order from 0 to 100
y = []
for j in range(0, 100):
    y.append(j)


p = figure(title="Plot Test", x_axis_label = "x", y_axis_label = "y")
p.line(x,y)

save(p)
