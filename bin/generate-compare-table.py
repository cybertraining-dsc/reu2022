import pandas as pd
from cloudmesh.common.util import writefile
from cloudmesh.common.util import readfile
from cloudmesh.common.console import Console
import yaml
from pprint import pprint
import os

filename = 'data/compare-graphics'

content = readfile(f'{filename}.yaml')
# print (content)

d = yaml.safe_load(content)


#pprint (d)

df = pd.DataFrame(d)
df = df.set_index('Value')
df = df.transpose()

# print(df)

content = df.to_markdown()
writefile(f'{filename}.md', content)

Console.ok(f'File {filename}.md created')

#d = df.to_dict(orient='list')
# pprint(d)


#with open(f'{filename}.yaml', 'w') as file:
#    documents = yaml.dump(d, file)
