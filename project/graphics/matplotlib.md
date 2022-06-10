## Matplotlib

Matplotlib is the main plotting library that allows the user to
visualize data. Matplotlib creates figures that can be manipulated and
transformed. This includes manipulations of axes, labels, fonts, and
the size of the images.

### Installation

To install matplotlib, please use the command:

```bash
$ pip install matplotlib
```

### Import Statements

The user will need to supply these import statements at the top of
their code in order for Matplotlib to be imported.

```python
import matplotlib.pyplot as plt
import numpy as np
```

### Bar Chart

In Matplotlib, it is easy to create bar charts. For example, this is a
demonstration of a simple bar chart using data from a user using
Spotify.

```python
import matplotlib.pyplot as plt

# you can also do this: from matplotlib import pyplot as plt

data = {'Rock': 136, 'Rap': 112, 'Folk': 110, 'Indie': 90, 'Jazz': 25}
categories = data.keys()
count = data.values()

# Creating the bar chart
plt.bar(categories,
        count,
        align='center',
        color='darkorange',
        width=0.4,
        edgecolor="royalblue",
        linewidth=4)

# Editing the bar chart's title, x, and y axes
plt.xlabel("Genre of Music")
plt.ylabel("Number of songs in the genre")
plt.title("Distribution of Genres in My Liked Songs")
plt.show()
```

This program can be downloaded from
[GitHub](https://github.com/cybertraining-dsc/reu2022/tree/main/project/graphics/examples/matplotlib-barchart.py). The output of this program is showcased in [@fig:matplotlib-barchart].

![Matplotlib Barchart created from data from Spotify.](examples/images/matplotlib-barchart.svg){#fig:matplotlib-barchart width=50%}

### Line Chart

The Matplotlib library in python allows for comprehensive line plots
to be created. Here a line chart was created using a for loop to
generate random numbers in a range and plot it against the `x` and `y`
axis to display the changes between two variables/data sets.

```python
import matplotlib.pyplot as plt
import random

x = []
y = []
for i in range(0, 100):
  x.append(i)
  value = random.random() * 100
  y.append(value)

# creating the plot and labeling axes and title
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Plot Test")
plt.show()
```

This program can be downloaded from
[GitHub](https://github.com/cybertraining-dsc/reu2022/tree/main/project/graphics/examples/matplotlib-linechart.py)
.
The output of this program is showcased in
[@fig:matplotlib-linechart].

![Matplotlib Linechart created from random variables](examples/images/matplotlib-linechart.svg){#fig:matplotlib-linechart width=50%}

### Pie Chart

A pie chart is most commonly used when representing the division of
components that form a whole thing e.g. showing how a budget is broken
down into separate spending categories. In Matplotlib, the function
`pie()`creates a pie chart. In the following code example, a user's
Spotify data will be displayed as a pie chart.

```python
import matplotlib.pyplot as plt

data = {'Rock': 136, 'Rap': 112, 'Folk': 110, 'Indie': 90, 'Jazz': 25}
categories = data.keys()
count = data.values()

# Creating the pie chart
plt.pie(count, labels=categories)

plt.show()
```

This program can be downloaded
from [GitHub](https://github.com/cybertraining-dsc/reu2022/tree/main/project/graphics/examples/matplotlib-piechart.py)

The output of this program is showcased in [@fig:matplotlib-piechart].

![Barchart created from data from Spotify](examples/images/matplotlib-piechart.svg){#fig:matplotlib-piechart width=50%}

### Contour Plot

Unlike the previous types of plots shown, contour plots allow data
involving three variables to be plotted on a 2D surface. In this
example, an equation of a hyperbolic paraboloid is graphed on a
contour plot.

```python
import matplotlib.pyplot as plt
import numpy as np

# creating an equation for z based off of variables x,y
x, y = np.meshgrid(np.linspace(-10, 10), np.linspace(-10, 10))
z = 9 * (x ** 2 + 1) + 8 * x - (y ** 2)
levels = np.linspace(np.min(z), np.max(z), 15)

# creating a contour graph based off the equation of z
plt.contour(x, y, z, levels=levels)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Function of z(x,y)")
plt.show()
```

This program can be downloaded from
[GitHub](https://github.com/cybertraining-dsc/reu2022/tree/main/project/graphics/examples/matplotlib-contour.py)
.
The output of this program is showcased in
[@fig:matplotlib-contourplot].

![Multivariable (x, y, z) Equation Plotted](examples/images/matplotlib-contour.svg){#fig:matplotlib-contourplot width=50%}

A contour plot allows data and equations consisting of three variables
to be plotted through plotting 3D surfaces as 2D slices on a `xy`
plane. Matplotlib can display data and equations through contour
graphs after they are inputted. Shown below are the parameters for
`plt.contour`.

```python
plt.contour([x, y], z, levels)
```

The independent variables `x` and `y` must be defined so the dependent
variable `z` can be defined. The variables can come in the form of a
list or dictionary or as an equation. The `levels` parameter
determines the number of contour lines that can be drawn.

### Titles, Labels, and Legends

#### Titles

Titles are necessary to let the reader know about your graph or plot
is exactly about. To give a title to your whole graph in matplotlib,
simply type:

```python
plt.title("Title you want to set").
```

#### x-axis labels and y-axis labels

Within the Matplotlib library are the functions `plt.xlabel()` and
`plt.ylabel()`. All these functions do is set a string to the two
axes. To use these functions, simply type:

```python
plt.xlabel("Label you want to set")
plt.ylabel("Label you want to set")
```

#### Legend

Sometimes, a legend may be necessary to let the reader know which part
of the graph/plot corresponds to each part of the data shown. To show
a legend, use the command:

```python
plt.legend()
```

### Rotating Ticks

When a chart is created, ticks are automatically created on the
axes. By default, they are set horizontally; however, they can be
rotated using `plt.xticks(degrees)` for the `x-axis` or
`plt.yticks(degrees)` for the `y-axis`. This can be shown by this
simple
[example](https://github.com/cybertraining-dsc/reu2022/blob/main/project/graphics/examples/rotatingticks.py). The output is shown in [@fig:ticks].

```python
import matplotlib.pyplot as plt

x = range(0, 4)
y = x
plt.plot(x, y)

# Rotating Ticks
plt.xticks(rotation=90)
plt.yticks(rotation=45)

plt.xlabel('x values')
plt.ylabel('y values')
plt.title(r'$y=x$')
plt.show()
```

![`x-axis` ticks rotated by 90° and `y-axis` ticks rotated by 45 degrees](examples/images/matplotlib-rotatingticks.svg){#fig:ticks width=50%}

### Exporting

#### Saving Chart as Files After a chart is created and displayed, it

can be exported as a file outside the code using this command:

```python
plt.savefig("fname", dpi='figure')
```

The name and format of the file are set as a string using
`fname`. Make sure to specify the format of the file by using a `.`
after the file name and specify the type after such as `.pdf`, `.png`,
`svg`, etc.

The parameter `dpi` sets the DPI (Dots per Inch) of the image being
saved. Specify this number in the form of a float. For example, set
`dpi=300`.

Additionally, there is another way to save files that may be faster
than calling a specific method for each file. The following code
showcases this:

```python
import matplotlib.pyplot as plt
import os
from matplotlib import pyplot


def save():
  name = os.path.basename(__file__).replace(".py", "")
  plt.savefig(f'/filepath/{name}.png')
  plt.savefig(f'filepath/{name}.pdf')
  plt.savefig(f'filepath/{name}.svg')
  plt.show()
```

This code can be accessed on
[GitHub](https://github.com/cybertraining-dsc/reu2022/tree/main/project/graphics/examples/matplotlib-linechart.py)

#### Display

The very last command that should be written is `plt.show()`, as this
command displays the graph that you made. To show, simply type:

```python
plt.show()
```

### Matplotlib Sources

* <https://matplotlib.org/>
* <https://matplotlib.org/stable/api/pyplot_summary.html>
* <https://www.activestate.com/resources/quick-reads/what-is-matplotlib-in-python-how-to-use-it-for-plotting/>
* <https://www.geeksforgeeks.org/bar-plot-in-matplotlib/>

