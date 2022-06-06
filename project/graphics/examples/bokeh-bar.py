from bokeh.io import show, export_png, export_svg
from bokeh.plotting import figure
from selenium import webdriver
import chromedriver_binary

p = figure(title="Bar Chart")

# The line_width parameter sets the width of the line plot.
x = [1,2,3]
y = [1,2,3]
p.vbar(x, top = y, line_color = 'black')

#show(p)

export_png(p, filename="images/bokeh-bar.png")
export_svg(p, filename="images/bokeh-bar.svg")