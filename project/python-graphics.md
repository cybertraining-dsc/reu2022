# Python Graphics

Demonstrate a cool graphics example program. Make sure you do not plagiarize.
Do not duplicate what is already in the book. However you can improve waht is in the book

* matpplotlib
* seaborn
* bokeh

# matplotlib

* item 1
* item 2

[link](https://google.com)

![Figure: PyCharm](./PyCharm.png)

To do: plot area “ticks”, white background, font size, save as pdf/png, set png image to 300dpi. 
Matplotlib

## Quick Overview of matplotlib

In python, there are multiple tiers (levels) in the hierarchy of
code. These levels are libraries, packages, modules, and
files. Libraries are large collections of packages and modules. They
contain a plethora of code, typically with a purpose behind the
collection. For instance, matplotlib is a library that contains a
bunch of packages and modules that were coded to give the user the
capability of data visualization. Packages are smaller than libraries
and contain more specific code for a project. An example within
matplotlib is pyplot- which is the package that specifically contains
all of the code to create charts, graphs, pie plots, etc. Modules are
even smaller and contain more specific code. They are essentially the
same as files as far as I am aware. Files are the individual sections
of code- like what you would see on PyCharm- that contain the code
that is used for a specific section of something.

Matplotlib is a library that contains the capabilities for data
visualization. The library can create pie charts, bar charts, line
plots, and other graphs specifically for data visualization. Inside
the library is pyplot, the package that contains all of the code for
the graphs- specifically the functions that need to be called and the
parameters that the functions take. Matplotlib creates figures that
can be manipulated and thus transformed. It also can create axes,
which are the labels that go on to the figures that are created.

## How To Install matplotlib/Bokeh in PyCharm using Git Bash

First, make sure to update Python to its latest version and it’s
installed on PyCharm. As of writing this, the latest version of Python
is 3.10.4. With this specific method, make sure that Git is installed
and is the main shell path on PyCharm which can be configured in
Settings/Tools/Terminal/Application Settings/Shell path: where Git
Bash should be selected.  Next, on the top bar in PyCharm, go to
View/Tool Windows/Terminal. The command line interface in PyCharm
should show up on the bottom of the screen. Then type in the following
and press Enter after each line:

```bash
$ cd
```



$ pip install matplotlib

OR
$ pip install bokeh

Our Own Work:
Bar Chart: 

```python
data = {'Rock': 136, 'Rap': 112, 'Folk': 110, 'Indie': 90, 'Jazz': 25}
categories = data.keys()
count = data.values()

# Creating the bar chart
plt.bar(categories, count, align='edge', color='darkorange', width=0.4, edgecolor=
"royalblue", linewidth=4)

# Editing the bar chart's title, x, and y axes
plt.xlabel("Genre of Music")
plt.ylabel("Number of songs in the genre")
plt.title("Distribution of Genres in My Liked Songs")
plt.show()
```







Line Plot:

```python
x = []
for i in range(0, 100):
    value = random.random() * 10000
    x.append(value)

# creating a list of 100 numbers in order from 0 to 100
y = []
for j in range(0, 100):
    y.append(j)

# creating the plot and labeling axes and title
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Plot Test")
plt.show()
```


Pie Plot:

```python
data = {'Rock': 136, 'Rap': 112, 'Folk': 110, 'Indie': 90, 'Jazz': 25}
categories = data.keys()
count = data.values()
plt.pie(count, labels=categories)
plt.show()
```





Contour Plot:





Bar Chart matplotlib Summary
	I researched the bar chart, which is a graph that visualizes data by displaying the quantity of several variables through different sized rectangles. Matplotlib essentially creates the bar chart object as a figure, and then displays that figure on the computer. plt.barchart takes in a multitude of parameters. 

Here is a full list of the parameters (most used), from the matplotlib API online. 

plt.bar( x, height, width, bottom, align)

From the matplotlib.pyplot.bar API: “The bars are positioned at x with the given alignment. Their dimensions are given by height and width. The vertical baseline is bottom (default 0).” Additionally, most of the parameters can take either one value and apply to all of the bars displayed, or multiple values and apply the values to the corresponding bars. 

So, x is the parameter that represents each x coordinate (which is usually the each individual bar label), height represents the height of each bar, width represents the width of the bars, bottom represents the starting point of the bottom of the bars (default 0), and align represents how the x values line up with the bars themselves (either “center” or “edge” with “center” being the middle and “edge” being the left side of the bar). 

There are also optional parameters to take into account. These are color (sets the color of the bars, edgecolor (sets the color of the edge of the bars), linewidth (sets the width of the bar edges themselves- normally 0- no edge), tick_label (strings or list of strings that represents tick labels for the bars), xerr/yerr (adds error bars to the bar chart, if needed), ecolor (represents the color of the error bars), capsize (length of the error bars), log (sets x axis to be log scale), data (imports data instead of doing x and height), *kwargs (keyword arguments- essentially allows the programmer to edit the rectangles being created- not widely used unless absolutely necessary). 
Line Chart matplotlib Summary
The line chart using the matplotlib library allows for multiple data sets to be contrasted against each other in the same graph. The line chart is positioned based on the np.linspace which takes in two total parameters that determine the starting point and the end point and an optional parameter that defines the total generated sample between the start/end points. With this, the variables and data sets can be plotted and modified to shape the steepness of the curve and its growth rate–exponential, polynomial, logarithmic, s-curved etc.

x = np.linspace(start,end,samples between start-finish)
plt.plot(x, y)

	Instead of only plotting a linear line, there is a choice to include multiple points of x-values that relate to its corresponding y-values. As mentioned, functions can be incorporated to adjust the line's properties either by addition, subtraction, division or multiplication.
Optional parameters for better visualization in a line chart includes the modification of the linestyle, and can be adjusted based on the viewer's preference–dotted line, dashed, dashed with dots or none). 
	


Pie Chart matplotlib Summary
	The pie chart is a graph that visually displays multiple quantities of data as a proportion to the total amount, represented as the whole circle, with each quantity shown as a proportional slice of it. Matplotlib has the ability to display data through a pie chart as a figure after data is inputted. The command plt.pie takes in many parameters.

Here are some of the parameters used in plt.pie, from matplotlib API online, not all of them are shown here.

plt.pie(x, labels, colors, normalize, startangle, radius, center)

	So, x is the parameter that consists of the data being plotted, which should be in the form of a list or dictionary as it’ll be multiple quantities of data. Each slice of the pie can be labeled. To do so, labels must be in the form of a list of strings in the same corresponding order as the data. The sequence of colors of the slices can be set using the command plt.get_cmap(“Colors”). 
	There is also the choice of making the pie chart a full pie or not using normalize. Setting it to True, which is the default, makes it a full pie, False makes it not a full pie. The angle of the start of the pie, set counterclockwise from the x-axis can be set using startangle. The radius of the pie can be set using radius and setting it to a float. The coordinates of the center of the chart can be set in the form (float, float). 

Contour Plot matplotlib Summary
	A contour plot allows data and equations consisting of three variables to be plotted through plotting 3D surfaces as 2D slices on an xy plane. Matplotlib has the ability to display data and equations through contour graphs after they are inputted. Shown below are the parameters for plt.contour.

plt.contour([X, Y], Z, levels)

The independent variables X and Y must be defined so the dependent variable Z can be defined. The variables can come in the form of a list or dictionary or as an equation. The levels parameter determines the number of contour lines that can be drawn. 

Labels and Titles

X-labels and y-labels: 

	Within the matplotlib library are the functions plt.xlabel() and plt.ylabel(). All these functions do is set a string to the two axes. To use these functions, simply type:
	plt.xlabel(“Label you want to set”)
	plt.ylabel(“Label you want to set”)
Titles
	To title your graph in matplotlib, use the command plt.title(“Title you want to set”). 
Legend
	
Show



Bokeh
Overview
Bokeh is a Python library useful for generating visualizations for web browsers. It generates graphics for all types of plots and dashboards powered by JavaScript without the user’s need to write any JavaScript code.

The guide below will walk you through useful Bokeh commands and features.

Bokeh Plotting Interface
Bokeh.plotting is the library’s main interface. It allows you to generate plots easily by providing parameters such as axes, grids, labels.
List of useful + common features, use cases?
Plotting charts


from bokeh.io import show
from bokeh.plotting import figure

p = figure(title = "My Graph", x_range = [0,20], y_axis_label = "the y axis", height = 500)

# plotting a line from (0,0) to (20,20); any of the CSS colors can be used
p.line([0,20],[0, 20], color='indigo')
# plotting a point (circle) at (5,10)
p.circle(5,10, color = 'green')

show(p)

Figure: Function [figure — Bokeh 2.4.3 Documentation]


Some useful parameters from figure:
x_axis_label and y_axis_label: labels for the x and y axis
x_range and y_range: specifications for the range of the x and y axis
title: text title for your graph
width and height: width and height of your graph in pixels
TOOLS



Output_file Function
Outputs to a static HTML file with a specific name

from bokeh.plotting import output_file
output_file(“name.html”)

After importing the Bokeh plotting interface, you will be able to create different types of plots utilizing the figure created with the figure function.

Scatter Plot
The Bokeh library provides various marker shapes for marking points on the scatter plot. The example below demonstrates how to create a scatter plot with two points at locations (1,3) and (2,4) respectively with circular and square marker shapes. The size parameter controls the size of the marker.

Circle
p.circle([1,2], [3,4], size = 10)

Square
p.square([1,2], [3,4], size = 10)

The list of all possible marker types and the functions used to create them can be found here:
http://docs.bokeh.org/en/latest/docs/user_guide/plotting.html


Line Graphs
The library provides a series of functions for creating various types of line graphs ranging from a single line graph, step line graph, stacked line graph, multiple line graph and so on. You can create a simple linear line graph connecting the the points (1,1), (2,2) and (3,3) with the following. The line_width parameter sets the width of the line graph

x = [1,2,3]
y = [1,2,3]
p.line(x, y, line_width = 1)

You can find the source code for other types of line graphs here:
http://docs.bokeh.org/en/latest/docs/user_guide/plotting.html


Bar Graphs


Reference
http://docs.bokeh.org/en/latest/ -Bokeh Documentation






Seaborn

Initial Overview:

	Seaborn is another data visualization tool that relies heavily upon other libraries such as numpy, pandas, and matplotlib. Matplotlib creates graphs, but seaborn essentially does it a little bit better and in more detail. It is a library for creating statistical graphs- data scientists likely love seaborn as it provides many tools through which they could make better visualizations about data they are working on. 

	Seaborn can directly use numpy, pandas, and matplotlib to enhance its overall functionality. There are several different types of plots that can be made from seaborn. They are: relational, distributional, categorical, regression, and matrix plots. One can only assume from this that machine and deep learning algorithms can be trained by using seaborn!

	Seaborn can be installed in the exact same way as the other libraries installed earlier:


$ pip install seaborn


	This should allow the OS to take on the library and add it to the working environment. 

	Additionally, it is important to note that seaborn comes with a function called load_dataset which automatically loads data from a Github repository called mwaskom. This repository appears to have a ton of datasets to practice using seaborn with. 

	Finally, it is equally important to point out that seaborn utilizes dataframes in order to create the plots that it has been programmed to create. Dataframes are 2 dimensional data objects, much like tables. 

Our Code:





















Seaborn Sources:
https://seaborn.pydata.org/api.html
https://www.geeksforgeeks.org/python-seaborn-tutorial/
https://www.geeksforgeeks.org/introduction-to-seaborn-python/
https://www.geeksforgeeks.org/plotting-graph-using-seaborn-python/
https://stackoverflow.com/questions/30336324/seaborn-load-dataset
​​https://github.com/mwaskom/seaborn-data/blob/master/planets.csv


Gallery (images)





