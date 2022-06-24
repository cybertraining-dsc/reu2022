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
nodes = ['job-1', 'job-2', 'job-3','job-4', 'job-5']

edges = [('job-1', 'job-2'), ('job-2', 'job-3'), ('job-3', 'job-4'),
         ('job-4', 'job-5')]

# G.add_node('queue1', nodes_for_adding=nodes)  # adding a node
G.add_edges_from(edges)
# G.remove_node('job-1')  # super cool, it removes the node AND the edge associated with the node

print(G)
color_map = []
for n in nodes:
    color_map.append('lightblue')

<<<<<<< HEAD

# nx.draw(G)
# plt.show()
=======
nx.draw(G, node_color=color_map, with_labels=True)
plt.savefig('images/network.png')
plt.show()
>>>>>>> b889b97983671ad618b4a0b330469dfa981e3902
