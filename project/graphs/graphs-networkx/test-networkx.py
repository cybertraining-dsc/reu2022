import networkx as nx
from matplotlib import pyplot as plt

"""
    This is a python file to test how the networkx library functions. It will
    be relatively basic as we do not need to create overly complicated graphs for
    an overview.
"""

# creating the overall graph object. We can do things to it now
G = nx.Graph()

# creating a list of nodes and edges- you have to be extremely careful not to typo
nodes = {'job-1': 'ls', 'job-2': 'echo hello world', 'job-3': 'cd ~',
         'job-4': 'cd cm/cloudmesh-cc', 'job-5': 'pytest tests'}

edges = [('job-1', 'job-2'), ('job-2', 'job-3'), ('job-3', 'job-4'),
         ('job-4', 'job-5')]

G.add_node('queue1', nodes_for_adding=nodes)
G.add_edges_from(edges)
#G.remove_node('job-1')  # super cool, it removes the node AND the edge associated with the node

print(G)
print("Graph nodes: ", G.nodes)
print("Graph edges: ", G.edges)
print(G['job-2'])


# nx.draw(G)
# plt.show()