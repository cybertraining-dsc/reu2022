import graphviz

g = graphviz.Digraph('Colors', filename='color-graphviz.gv')
g.attr(bgcolor='red:pink', label='Red Graph', fontcolor='white')

with g.subgraph(name='cluster') as c:
    c.attr(color='cyan', style='filled', label='Cyan Cluster',
           fontcolor='white')
    c.node('n1', 'Orange Node', shape='circle', fillcolor='red:yellow',
           style='filled', gradientangle='90')
    c.node('n2', 'Yellow Node', shape='diamond', color='yellow', style='filled')
    c.edge('n2', 'n1', label='Edge 1')

g.view()