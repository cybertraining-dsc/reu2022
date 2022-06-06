from bokeh.io import show, export_png, export_svg
from bokeh.plotting import figure
from selenium import webdriver
import chromedriver_binary
import os

def save (p):
    name = os.path.basename(__file__).replace(".py", "")
    export_png(p, filename=f"images/{name}.png")
    export_svg(p, filename=f"images/{name}.svg")
    show(p)

data = {'Rock': 136, 'Rap': 112, 'Folk': 110, 'Indie': 90, 'Jazz': 25}
x = list(data.keys())
y = list(data.values())

p = figure(x_range = x, title="Bar Chart")

p.vbar(x=x, top = y, line_color = 'black',color='orange',
    width = 0.9,
    line_width = 2
       )

save(p)

