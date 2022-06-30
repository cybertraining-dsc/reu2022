import graphviz

s = graphviz.Digraph('files in directories', filename='structure-graphviz.gv')
s.node_attr={'shape' : 'record'}

s.node('s1', '<d1> cloudmesh-cc | <d2> workflow')
s.node('s2', '{<d1> cloudmesh | <d2> tests}')
s.node('s3', '<d1> contribute | {<d2> graphs |{<d3> graphviz | <d4> networkx}}')

s.edges([('s1:d1', 's2:d2'), ('s1:d2', 's3:d4')])

s.view()