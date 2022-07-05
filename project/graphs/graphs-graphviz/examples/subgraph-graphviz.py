import graphviz

g = graphviz.Digraph('jobs in queues', filename='subgraph-graphviz.gv')

with g.subgraph(name='cluster_1') as s:
    s.node('job-1', 'ls')
    s.node('job-2', 'echo hello world')
    s.node('job-3', 'cd')
    s.node('job-4', 'cd cm/cloudmesh-cc')
    s.node('job-5', 'pytest tests')
    s.edges([('job-1', 'job-2'), ('job-2', 'job-3'), ('job-3', 'job-4'),
             ('job-4', 'job-5')], )

with g.subgraph(name='cluster_2') as s:
    s.node('job-6', 'cd')
    s.node('job-7', 'cd cm')
    s.node('job-8', 'cd cm/cloudmesh-alex')
    s.node('job-9', 'git status')
    s.node('job-10', 'git pull')
    s.edges([('job-6', 'job-7'), ('job-7', 'job-8'), ('job-8', 'job-9'),
             ('job-9', 'job-10')], )

g.edge('start', 'job-1')
g.edge('start', 'job-6')
g.edge('job-5', 'end')
g.edge('job-10', 'end')
g.edge('job-3', 'job-7')
g.edge('job-4', 'job-9')

g.node('start', shape='square')
g.node('end', shape='square')

g.view()

