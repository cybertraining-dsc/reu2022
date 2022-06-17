# Yaml Database (yamldb)

Yamldb is a python package that allows a user to store variables on a computer's
hard-drive, as opposed to having variables stored in memory. 

Yamldb makes use of the yaml data file, and it stores values in the yaml files 
so that they can be easy to use. The yaml files can be accessed like python
dictionaries, which makes the process significantly easier for the user. 

The yamldb package is used in the `cloudmesh-cc` section of the `cloudmesh` 
repository and can be accessed [here](https://github.com/cloudmesh/cloudmesh-cc).

## Installing and importing

Yamldb is easy to install. Simply execute the following command:

```bash
pip install yamldb
```

Then, to import yamldb to a python file, simply execute the following code:

```python
from yamldb import YamlDB
```

Now, following these commands, the computer is set up to run and access yamldb. 

## Using yamldb

Yamldb has several methods within itself that allow the user easy access to 
creating a yaml file and storing things within it. These things can be anything,
really. The methods include: `Yamldb()`, `.get()`, `.load()`, `.save()`, and
`.search()`. All of these functions can be used. The following is example
code of how someone might use yamldb for their own code. 

```python
from yamldb import YamlDB

filename = 'PATH'
database = YamlDB(filename=filename)

database['queue1'] = 'job1'
database['queue2.job1'] = 'echo hello world'

d = database.get('queue1', default=3)
```
This code can be accessed from [GitHub](https://github.com/cybertraining-dsc/reu2022/tree/main/project/python/yamldb/yamldb-test.py).

Which creates:

```yaml
queue1: job1
queue2:
  job1: echo hello world
```
## Accessing Values
As one can see, these values are easy to access. Let's say, for instance, that
we were trying to access the `queue2:job1` string `"echo hello world"`. To do 
this, we would execute the following:

```python
job = database.get('queue2')
print(job)

command = database['queue2'].get('job1')
print(command)
```
This code can be accessed from [GitHub](https://github.com/cybertraining-dsc/reu2022/tree/main/project/python/yamldb/yamldb-test.py).


Which returns:

```bash
{'job1': 'echo hello world'}
echo hello world
```

## Save, Load, and Search

With the `yamldb` implementation, it is simple to save, load, and search. 
The following code shows this output. 

```python
from yamldb import YamlDB

filename = 'PATH'
database = YamlDB(filename=filename)

database['queue1'] = 'job1'
database['queue2.job1'] = 'echo hello world'

d = database.get('queue1', default=3)

database.load(filename)  # loads the file
database.save(filename)  # saves the file
database.search('queue1') # searches the file for the query
```
This code can be accessed from [GitHub](https://github.com/cybertraining-dsc/reu2022/tree/main/project/python/yamldb/yamldb-test.py).


The `.load()` function loads in the current `.yaml` file that was created 
originally. The `.save()` function saves the any updates that were made to the 
`.yaml` file. 

Outside of that, this should be the fully implementation of the `yamldb` 
python package.

The overview of this python package was accessed from [here](https://pypi.org/project/yamldb/).