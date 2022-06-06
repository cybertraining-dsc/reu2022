from bokeh.io import show, export_png
from bokeh.plotting import figure, output_file

# labeling the title, specifying the range of the x-axis, labeling the y-axis, specifying the height to be 500 pxls
p = figure(title = "My Graph", x_range = [0,20], y_axis_label = "the y axis", height = 500)

# plotting a line from (0,0) to (20,20); any of the CSS colors can be used
p.line([0,20],[0, 20], color='indigo')

# plotting a point (circle) at (5,10)
p.circle(5,10, color = 'green')

#show(p)

export_png(p, filename="plot.png")
export_svgs(p, filename="plot.svg")
