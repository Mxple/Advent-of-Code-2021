import os, sys, networkx as nx, matplotlib.pyplot as plt
from networkx.algorithms.components.connected import node_connected_component

with open(os.path.join(sys.path[0], "input.txt"), "r") as file:
    data = file.read().replace("-"," ").splitlines()

print(data)
g = nx.Graph()
for path in data:
    g.add_edge(path.split()[0],path.split()[1])

color_map = []
for node in g:
    if node.isupper():
        color_map.append("#f54275")
    elif node == "start" or node == "end":
        color_map.append("#eb6b3d")
    else:
        color_map.append("#4287f5")

nx.draw(g, with_labels=True, node_color=color_map)
plt.show()