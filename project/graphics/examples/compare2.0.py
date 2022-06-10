import pandas as pd
from cloudmesh.common.util import writefile
import yaml
from pprint import pprint


filename = 'compare-graphics'
df = pd.read_csv(f'{filename}.csv')
print(df)
df = df.set_index('Value')

content = df.to_markdown()
writefile(f'{filename}.md', content)

d = df.to_dict(orient='list')
# pprint(d)


with open(f'{filename}.yaml', 'w') as file:
    documents = yaml.dump(d, file)
