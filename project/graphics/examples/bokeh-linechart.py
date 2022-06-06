from bokeh.io import show, export_png, export_svg
from bokeh.plotting import figure
from selenium import webdriver
import chromedriver_binary

p = figure(title="Line Plot")

# The line_width parameter sets the width of the line plot.
x = [1,2,3]
y = [1,2,3]
p.line(x, y, line_width = 1)

# show(p)

export_png(p, filename="images/bokeh-line.png")
export_svg(p, filename="images/bokeh-line.svg")