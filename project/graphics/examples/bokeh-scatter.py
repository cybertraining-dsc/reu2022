from bokeh.io import show, export_png, export_svg
from bokeh.plotting import figure
from selenium import webdriver
import chromedriver_binary

p = figure(title="Scatter Plot")

# Circle
p.circle([0,3], [4,5], size = 10)

# Square
p.square([1,2], [3,4], size = 10)

# show(p)

export_png(p, filename="images/bokeh-scatter.png")
export_svg(p, filename="images/bokeh-scatter.svg")