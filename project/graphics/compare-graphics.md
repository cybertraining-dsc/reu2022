# Comparison Table

Although Matplotlib is the main plotting interface, several other libraries include simple visualization options. We
have created a comparison table to showcase the differences between Matplotlib, Seaborn, Bokeh, and Pandas.

```python

import matplotlib as plt
import pandas as pd

df = pd.DataFrame()

```

| Value               | matlotlib    | seaborn | bokeh | pandas                                                                                                                        |
|---------------------|--------------|---------|-------|-------------------------------------------------------------------------------------------------------------------------------|
| **charts**          |
| barchart            | plt.bar(...) | +       | +     | [df.plot.bar(...)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.bar.html)                 |
| grouped barchart    |              |         |       | [df.plot.bar(...)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.bar.html)                 |
| stacked barchart    |              |         |       | [df.plot.bar(stacked=True)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.bar.html)        |
| spline chart        |              |         |       |                                                                                                                               |
| multiline chart     |              |         |       |                                                                                                                               |
| compound line chart |              |         |       |                                                                                                                               |
| histogram           |              |         |       |                                                                                                                               |
| linechart           | +            | +       | +     | [df.plot.line(...)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.line.html)               |
| scatterplot         | +            | +       | +     | [df.plot.scatter(...)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.scatter.html)         |
| piechart            | +            |         | +     | [df.plot.pie(...)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.pie.html)                 |
| exploded piechart   |              |         |       | -                                                                                                                             |
| donutchart          |              |         |       | -                                                                                                                             |
| countourplot        | +            | +       |       | -                                                                                                                             |
| distributionplot    | +            | +       |       | +                                                                                                                             |
| point chart         |              |         |       |                                                                                                                               |
| scatterplot         |              |         |       |                                                                                                                               |
| bubblechart         |              |         |       | [df.plot.scatter(s=...,c=...)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.scatter.html) |
| radar chart         |              |         |       | -                                                                                                                             |
| boxplot             |              |         |       | [df.plot.boxplot(...)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.boxplot.html)              |
| **features**        |
| easy png export     | +            | +       |       | +                                                                                                                             |
| color palettes      |              | +       |       |                                                                                                                               |
| interactive graph   |              |         | +     |                                                                                                                               |
| data frame          |              |         |       | [df](tbd)                                                                                                                     |
| Value               | matlotlib                                                                                                                    | seaborn | bokeh | pandas                                                                                                        |
|---------------------|------------------------------------------------------------------------------------------------------------------------------|---------|-------|---------------------------------------------------------------------------------------------------------------|
| **charts**          |
| barchart            | [plt.bar(...)](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.bar.html#matplotlib.axes.Axes.bar)             | +       | +     | [df.plot.bar(...)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.bar.html) |
| grouped barchart    |                                                                                                                              |         |       |                                                                                                               |
| stacked barchart    |                                                                                                                              |         |       |                                                                                                               |
| spline chart        |                                                                                                                              |         |       |                                                                                                               |
| multiline chart     |                                                                                                                              |         |       |                                                                                                               |
| compound line chart |                                                                                                                              |         |       |                                                                                                               |
| histogram           | [plt.hist(...)](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist.html#matplotlib.axes.Axes.hist)          |         |       |                                                                                                               |
| linechart           | [plt.plot(...)](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot)          | +       | +     | +                                                                                                             |
| scatterplot         | [plt.scatter(...)](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter) | +       | +     | +                                                                                                             |
| piechart            | [plt.pie(...)](https://matplotlib.<br/>org/stable/api/_as_gen/matplotlib.axes.Axes.pie.html#matplotlib.axes.Axes.pie)        |         | +     | +                                                                                                             |
| exploded piechart   |                                                                                                                              |         |       |                                                                                                               |
| donutchart          |                                                                                                                              |         |       |                                                                                                               |
| countourplot        | [plt.contour(...)](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.contour.html#matplotlib.axes.Axes.contour) | +       |       |                                                                                                               |
| distributionplot    | +                                                                                                                            | +       |       | +                                                                                                             |
| point chart         |                                                                                                                              |         |       |                                                                                                               |
| scatterplot         | [plt.scatter(...)](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter) |         |       |                                                                                                               |
| bubblechart         |                                                                                                                              |         |       |                                                                                                               |
| radar chart         |                                                                                                                              |         |       |                                                                                                               |
| boxplot             | [plt.boxplot(...)](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html#matplotlib.axes.Axes.boxplot) |         |       |                                                                                                               |
| **features**        |
| easy png export     | +                                                                                                                            | +       |       | +                                                                                                             |
| color palettes      |                                                                                                                              | +       |       |                                                                                                               |
| interactive graph   |                                                                                                                              |         | +     |                                                                                                               |
| data frame          |                                                                                                                              |         |       | [df](tbd)                                                                                                     |


The full set of graphing options for Matplotlib is displayed in the 
[Matplotlib Gallery](<https://matplotlib.org/3.3.0/gallery/index.html>).

While Matplotlib has the most options for all varieties of graphs, Seaborn specializes in color palettes for such graphs
while Bokeh's specialty is an interactive `.html` graph that opens in the web browser and can be scrolled and explored.

Meanwhile, Pandas is a very popular data manipulation tool. Its special feature is the data frame, a special way to
store data. Thus, visualizing data created through Pandas requires understanding how data frames work.

Next is a tutorial on some simple visualization tools we can use with each library.


