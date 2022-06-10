import pandas as pd
from cloudmesh.common.util import writefile
from cloudmesh.common.util import readfile
import yaml
from pprint import pprint


filename = 'data/compare-graphics'

content = readfile(f'{filename}.yaml')
print (content)

d = yaml.safe_load(content)


pprint (d)

#df = pd.read_csv(f'{filename}.csv')
#print(df)
#df = df.set_index('Value')

#content = df.to_markdown()
#writefile(f'{filename}.md', content)

#d = df.to_dict(orient='list')
# pprint(d)


#with open(f'{filename}.yaml', 'w') as file:
#    documents = yaml.dump(d, file)
