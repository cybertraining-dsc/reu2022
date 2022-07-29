# Python Data Management for Visualizations

In python, there are several ways that data can be interpreted in order to
generate the graphics for data visualization.

Through several examples, we will show how to manage different types of data and
how to best interact with them. They are lists, dictionaries and CSV files.

## Lists

Lists are clumps of continuous values that are put directly next to each other
in the computer memory system.

### Construction

In python, lists can be constructed like this:

```python
example_list = ['example', 2, 'b', 45, False]
```

Lists have order and can hold many types (bool, int, String, etc.) of values.

### Accessing Values

In python, it is easy to access values within a list. The following code
provides an example of how to access certain values within a list:

```python
index_4 = example_list[4]
print(index_4)
# output is False
```

It is important to note that lists have indices, which range from 0 to the
length of the list - 1. The indices provide access to values within the list.

### Updating Values

To update a value within a list, simply utilize same brackets:

```python
example_list[3] = 'bear'
print(example_list[3])
# output is 'bear' instead of 45
```

This will change the value at the third index from 45 to bear.

### Python Built-In Methods

Python has several built-in methods for lists. These include `append()`
, `clear()`
`copy()`, `count()`, `extend()`, `index()`, `insert()`, `pop()`, `remove(`
, `reverse()`, and `sort()`.

A user can utilize these methods to make changes in the necessary ways to the
list.

## Dictionaries

Dictionaries are like specialized lists. They hold a key-value pair that allows
for a user to look up a key and find the associated value. Dictionaries are
useful for storing values in a way that is more organized than a linear list.
Furthermore, dictionaries make it easy for users to look up the necessary
information.

### Construction

In python, dictionaries are constructed as follows:

```python
example_dictionary = {'motorcycles': 2, 'autocycles': 3,
                      'cars': 4, 'small_trucks': 6
                      'large_trucks': '18'}
```

The string values are the keys, which provide access to the values within the
dictionary. The colon provides the computer with the command for assigning
key-value pair.

### Accessing Values

There are several built-in commands to access both the keys and values in a
dictionary. They are as follows:

```python
example_dictionary.get()
example_dicionary.keys()
example_dictionary.values()
```

The `.get()` method returns the value that is associated with the given key,
the `.keys()` method returns a list of the keys alone, and the `.values()`
method returns a list of the values alone. There are more methods (see the
Python Built-In Methods section)

### Updating Values

To update the dictionary, there is one method that can be used:

```python
example_dictionary.update({'motorcycles': 20})

# or to add a new key-value pair to the dictionary:

example_dictionary['New Key'] = 'New Value'
```

This will update the value associated with this particular key-value pair.

### Python Built-In Methods

There are several built-in methods that allow for more dictionary manipulation:
They are `clear()`, `copy()`, `fromkeys()`, `items()`,
`pop()`, `popitem()`, and `setdefault()`.

## CSV Files

CSV stands for *comma-separated-values* and is a data structure that is
incredibly common for data management and analysis. There are many ways to
access CSV files. The most common way is to use pandas, a python library.
However, python also has a built-in CSV module that can be used. We will show
examples of using both below.

### Installing and Importing

Before beginning with any of these CSV manipulation tasks, it is necessary to
install and import the correct modules and libraries. The following showcases
this:

```bash
$ pip install pandas
```

```python
import pandas as pd
import csv
```

### Construction

CSV files are files that exist elsewhere and have already been created.
Therefore, for creation, we are not creating a CSV files, but rather
deconstructing it into something that is usable.

In pandas, this means creating a dataframe, which is essentially and indexed
table. In the python `csv` module, this means using the
`csvreader` object within the module. Following are two examples showcasing how
exactly to do this.

For the `csv` module:

```python
# open the csv and creates the reader object for it
file = open('/Users/jacksonmiskill/Downloads/biostats.csv')
reader = csv.reader(file)
```

The `reader` is an object that was created by python developers to help parse
through the `csv` files.

For the `pandas` module:

```python
file = pd.read_csv("/Users/jacksonmiskill/Downloads/biostats.csv")
df = pd.DataFrame(file)
```

### Accessing Values

For the `csv` module:

It is more challenging to access files using the `csv` module as opposed to
the `pandas` library. To make it more simple, it is necessary to convert the
values that lie within the `csv` into a list in order to access.

```python
data = []
for each_row in reader:
    data.append(each_row[2])

print(data)  # output is the whole list
```

This code is available
on [GitHub](https://github.com/cybertraining-dsc/reu2022/blob/main/project/graphics/data-management/python-data.py)

For the `pandas` module, it is less complicated to access that values. This is
because the module includes a function that converts the data into a dataframe.
After converting, you can use the various methods that are within the dataframe
to essentially pass in the correct values.

### Examples

Once the `csv` values have been accessed, creation of the graphics can begin.
Starting with the `csv` module and then moving into `pandas`
the following will demonstrate this action.

The `csv` file that will be utilized for the following examples can be found
[here](https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html). It represents
made up data on a group of made up people such as age, height, and weight.

It is slow and complicated to create graphs with the `csv`
module. We have implemented a separate module called `ConvertCSV` which provides
the user with the ability to convert the data received from the
`csv` module into doubly nested lists, lists, and dictionaries, depending on
necessity.

```python
# reading in the data!
filename = path_expand("./biostats")
table = ConvertCSV.create_table(filename)
print(table)

list_names = []
list_heights = []

list_names = ConvertCSV.csv_read_to_list(table=table, index=0, convert=False)
list_heights = ConvertCSV.csv_read_to_list(table=table, index=3, convert=True)

dict_names = []
dict_heights = []

idict = ConvertCSV.csv_read_to_dict(table=table, index=3)
dict_names = list(idict.keys())
dict_heights = list(idict.values())

# now just plot these values. You can use whichever library you desire
# for the example, we use matplotlib, because it is simple

# list
plt.plot(list_names, list_heights)
plt.xlabel("Names")
plt.ylabel("Heights")
plt.xticks(rotation=90)
plt.savefig('images/csv-list-lineplot.png')
plt.savefig('images/csv-list-lineplot.svg')
plt.savefig('images/csv-list-lineplot.pdf')
plt.title("Names and Corresponding Height")
plt.show()

# dictionary
plt.plot(dict_names, dict_heights)
plt.xlabel("Names")
plt.ylabel("Heights")
plt.xticks(rotation=90)
plt.savefig('images/csv-dict-lineplot.png')
plt.savefig('images/csv-dict-lineplot.svg')
plt.savefig('images/csv-dict-lineplot.pdf')
plt.title("Names and Corresponding Height")
plt.show()
```

This code can be access from
[GitHub](https://github.com/cybertraining-dsc/reu2022/blob/main/project/graphics/data-management/python-data.py)

This code produces [@fig:csv-list-lineplot]. and Figure [@fig:csv-dict-lineplot].:

{#fig:csv-list-lineplot width=50%}

[@fig:csv-list-lineplot]: created using the data
available [here](https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html).

{#fig:csv-dict-lineplot width=50%}

[@fig:csv-dict-lineplot]: created using the data
available [here](https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html).

However, it is so much more simple to accomplish this with the `pandas`
library:

```python
file = pd.read_csv("/Users/jacksonmiskill/Downloads/biostats.csv")
biostats = pd.DataFrame(file)

plt.plot(biostats['Name'], biostats[' "Height (in)"'])
plt.xlabel("Name")
plt.ylabel("Height")
plt.xticks(rotation=90)
plt.savefig('images/pandas-lineplot.png')
plt.savefig('images/pandas-lineplot.svg')
plt.savefig('images/pandas-lineplot.pdf')
plt.title("Names and Corresponding Height")
plt.show()
```

This code can be accessed from
[GitHub](https://github.com/cybertraining-dsc/reu2022/blob/main/project/graphics/data-management/python-data.py)

This code produces the [@fig:pandas-lineplot]:

{#fig:pandas-lineplot width=50%}

[@fig:pandas-lineplot]: created using the data
available [here](https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html).

## Links

### Lists

* [List Manipulation](<https://towardsdatascience.com/python-basics-6-lists-and-list-manipulation-a56be62b1f95>)
* [Python List and Array Methods](<https://www.w3schools.com/python/python_ref_list.asp>)

### Dictionaries

* [Dictionary Manipulation in Python](<https://www.pythonforbeginners.com/dictionary/dictionary-manipulation-in-python>)
* [Python Dictionary Methods](<https://www.w3schools.com/python/python_ref_dictionary.asp>)
* [Update a dictionary](<https://www.w3schools.com/python/ref_dictionary_update.asp>)

### CSV Files

* [Create a dataframe](<https://www.geeksforgeeks.org/creating-a-dataframe-using-csv-files/>)
* [CSV File Reading and Writing](<https://docs.python.org/3/library/csv.html#examples>)
* [CSV File Overview](<https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html>)
* [Python Built in Read CSV Files](<https://docs.python.org/3/library/functions.html#open>)
* [Extracting Information from a CSV File](<https://www.protechtraining.com/blog/post/python-for-beginners-reading-manipulating-csv-files-737#extracting-information-from-a-csv-file>)
* [List Index out of Range](<https://stackoverflow.com/questions/13039392/csv-list-index-out-of-range>)
* [Visualizing Data in CSV](<https://www.geeksforgeeks.org/visualize-data-from-csv-file-in-python/>)