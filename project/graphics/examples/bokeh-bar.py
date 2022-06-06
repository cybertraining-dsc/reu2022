from bokeh.io import show, export_png, export_svg
from bokeh.plotting import figure
from selenium import webdriver
import chromedriver_binary


data = {'Rock': 136, 'Rap': 112, 'Folk': 110, 'Indie': 90, 'Jazz': 25}
x = list(data.keys())
y = list(data.values())
z = [1,2,3]

p = figure(x_range = x, title="Bar Chart")

print(type(x))
print(type(y))
print(type(z))
print(x)
print(y)
print(z)

p.vbar(x=x, top = y, line_color = 'black',color='orange',
    width = 0.9,
    line_width = 2
       )



show(p)

export_png(p, filename="images/bokeh-bar.png")
export_svg(p, filename="images/bokeh-bar.svg")


