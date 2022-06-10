import pandas as pd
from cloudmesh.common.util import writefile

filename = 'compare-graphics'
df = pd.read_csv(f'{filename}.csv')

content = df.to_markdown()
writefile(f'{filename}.md', content)