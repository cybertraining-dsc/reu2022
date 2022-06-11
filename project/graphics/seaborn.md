# Seaborn

Seaborn, like Matplotlib, is a data visualization tool. However, the
graphs and charts that Seaborn can create are more complex than
Matplotlib. The graphs that are created in Seaborn are more
statistically detailed. Unlike matplotlib, Seaborn draws upon other
imported libraries such as Matplotlib, Numpy, and Pandas. This is
because Seaborn relies on more complex math (Numpy) and data frames
(generated from Pandas) that are passed into its functions as the
data.

Several types of plots can be made from Seaborn; they are relational,
distributional, categorical, regression, and matrix plots.

We have created examples to demonstrate the abilities of Seaborn.

## Installation

Seaborn can be installed in the same way as the other libraries
installed earlier. The user who is installing the library should make
sure that it is being installed in the correct environment.

```bash
$ pip install seaborn
```

## Import Statements

The user will need to supply these import statements at the top of
their code in order for Seaborn to be imported. Additionally, the
data created for the examples represents a user's Liked songs from
Spotify.

```python
import seaborn as sns
import matplotlib.pyplot as plt

data = {'Rock': 136, 'Rap': 112, 'Folk': 110, 'Indie': 90, 'Jazz': 25}
categories = list(data.keys())
count = list(data.values())
personal_rank = [3, 4, 2, 1, 5]
```

## Relational Plots

Relational plots showcase the relationship between variables in a
visual format. It is a broad term for data representation. Examples of
relational plots in Seaborn are `relplot` `lineplot` and
`scatterplot`.

It is simple to create a relational plot with Seaborn:

```python
sns.relplot(x=months, y=photos)
plt.xlabel("Month of the year")
plt.ylabel("Amount of photos taken")
plt.show()
```

This program can be downloaded from
[GitHub](https://github.com/cybertraining-dsc/reu2022/blob/main/project/graphics/examples/seaborn-images.py)
. The output of this program is showcased in[@fig:seaborn-lineplot].

![Seaborn Lineplot created from user Spotify data.](examples/images/seaborn-lineplot.svg){#fig:seaborn-lineplot width=50%}

## Distribution Plots

A distribution plot shows how the data is concentrated in a range of
values. The graph that appears looks similar to a bar graph in that
there are bars. However, these bars show the concentration of a
variable across a range of values rather than the quantity possessed
by a singular variable. The distributional plots in Seaborn are
`displot` `histplot` `kdeplot` `ecdfplot` and `rugplot`.

```python
sns.displot(x=source, y=value)
plt.show()
```

This program can be downloaded from
[GitHub](https://github.com/cybertraining-dsc/reu2022/blob/main/project/graphics/examples/seaborn-images.py)
. The output of this program is showcased in [@fig:seaborn-displot]

![Seaborn Displot created from user Spotify data](examples/images/seaborn-displot.svg){#fig:seaborn-displot width=50%}

## Categorical Plots

Categorical plots are statistical graphs that help visualize the
magnitudes of different variables in a dataset. A type of categorical
plot is a bar chart, exactly like the example produced in the
Matplotlib section. The categorical plots are `catplot` `stripplot`
`swarmplot` `boxplot` `violinplot` `boxenplot` `pointplot` `barplot`
and `countplot`.

Categorical plots are relatively simple to implement. If using the
`catplot` method, it is necessary to include the `kind` parameter.

```python
sns.barplot(x=source, y=value)
plt.show()
```

This program can be downloaded
from [GitHub](https://github.com/cybertraining-dsc/reu2022/blob/main/project/graphics/examples/seaborn-images.py)

The output from the program is showcased in [@fig:seaborn-catplot]

![Seaborn Catplot created from user Spotify data.](examples/images/seaborn-catplot.svg){#fig:seaborn-catplot width=50%}

## Regression Plots

Regression plots are like relational plots in the way that they help
visualize the relationship between two variables. Regression plots,
however, show the linear correlation that may or may not exist in a
scatter plot of data. Their regression plots are `lmplot` `regplot`
and `residplot`.

Regression plots are simple to implement:

```python
sns.regplot(x=months, y=photos)
plt.show()
```

This program can be downloaded from
[GitHub](https://github.com/cybertraining-dsc/reu2022/blob/main/project/graphics/examples/seaborn-images.py)
. The output of this program is showcased in [@fig:seaborn-regplot].

![Seaborn regplot created from user Spotify data](examples/images/seaborn-regplot.svg){#fig:seaborn-regplot width=50%}

Each of these plots can be manipulated to the users needs via the API
that is listed in the sources section.

## Saving Figures

Saving figures created by Seaborn is quite simple. This is because it
is the exact same as in Matplotlib.

To save a figure:

```python
plt.savefig('figure_path/figure_name')
```

This program can be downloaded from
[GitHub](https://github.com/cybertraining-dsc/reu2022/blob/main/project/graphics/examples/seaborn-images.py)

## Links

* <https://seaborn.pydata.org/api.html>
* <https://www.geeksforgeeks.org/python-seaborn-tutorial/>
* <https://www.geeksforgeeks.org/introduction-to-seaborn-python/>
* <https://www.geeksforgeeks.org/plotting-graph-using-seaborn-python/>
* <https://stackoverflow.com/questions/30336324/seaborn-load-dataset>
* <https://github.com/mwaskom/seaborn-data/blob/master/planets.csv>