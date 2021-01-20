# -*- coding: utf-8 -*-



### Asia Network 

import networkx as nx
import matplotlib.pyplot as plt

g1 = nx.Graph()

g1.add_edge("Indonesia", "Singapore", weight = 0.14)
g1.add_edge("China", "United States", weight = 0.18)
g1.add_edge("Japan", "United States", weight = 0.14)
g1.add_edge("China", "Vietnam", weight = 0.09)
g1.add_edge("India", "Singapore", weight = 0.10)
g1.add_edge("China", "Japan", weight = 0.09)
g1.add_edge("China", "Singapore", weight = 0.09)
g1.add_edge("France", "India", weight = 0.08)
g1.add_edge("Singapore", "Thailand", weight = 0.07)
g1.add_edge("Singapore", "Vietnam", weight = 0.04)

g1.large = [(u, v) for (u, v, d) in g1.edges(data=True) if d["weight"] > 0.08]
g1.small = [(u, v) for (u, v, d) in g1.edges(data=True) if d["weight"] <= 0.08]

# positions for all nodes
pos = nx.spring_layout(g1)  

# nodes
nx.draw_networkx_nodes(g1, pos, node_size = 50)

# edges
nx.draw_networkx_edges(g1, pos, edgelist = g1.large, width=2, edge_color = "red")
nx.draw_networkx_edges(g1, pos, edgelist = g1.small, width=2, alpha=0.5, 
                       edge_color="blue")

# labels
nx.draw_networkx_labels(g1, pos, font_size=10, font_family="sans-serif")

plt.axis("off")
plt.show()


## Network Analysis
g1.degree()



### Africa network 

import networkx as nx 
import matplotlib.pyplot as plt


#weighted graph 
g2 = nx.Graph()

g2.add_edge("Egypt", "France", weight = 0.18)
g2.add_edge("South Africa", "United Kingdom", weight = 0.16)
g2.add_edge("Algeria", "France", weight = 0.13)
g2.add_edge("Morocco", "France", weight = 0.10)
g2.add_edge("Morocco", "Spain", weight = 0.09)
g2.add_edge("Morocco", "United Kingdom", weight = 0.09)
g2.add_edge("Nigeria", "United Kingdom", weight = 0.08)
g2.add_edge("Algeria", "Spain", weight = 0.03)
g2.add_edge("Algeria", "Italy", weight = 0.08)
g2.add_edge("Egypt", "Italy", weight = 0.06)

g2.large = [(u, v) for (u, v, d) in g2.edges(data=True) if d["weight"] > 0.08]
g2.small = [(u, v) for (u, v, d) in g2.edges(data=True) if d["weight"] <= 0.08]

 # positions for all nodes
pos = nx.spring_layout(g2) 

# nodes
nx.draw_networkx_nodes(g2, pos, node_size = 50)

# edges
nx.draw_networkx_edges(g2, pos, edgelist = g2.large, width=2, edge_color = "red")
nx.draw_networkx_edges(g2, pos, edgelist = g2.small, width=2, alpha=0.5, 
                       edge_color="blue")

# labels
nx.draw_networkx_labels(g2, pos, font_size=10, font_family="sans-serif")

plt.axis("off")
plt.show()


## Network Analysis
g2.degree()



### Oceania Network 

import networkx as nx 
import matplotlib.pyplot as plt


#weighted graph 
g3 = nx.Graph()

g3.add_edge("Australia", "United States", weight = 0.48)
g3.add_edge("Australia", "New Zealand", weight = 0.19)
g3.add_edge("Australia", "Singapore", weight = 0.08)
g3.add_edge("Australia", "Japan", weight = 0.08)
g3.add_edge("New Zealand", "United States", weight = 0.08)
g3.add_edge("Australia", "China", weight = 0.07)
g3.add_edge("Australia", "Indoneisa", weight = 0.01)
g3.add_edge("Australia", "Fiji", weight = 0.0046)
g3.add_edge("Australia", "Papa New Guinea", weight = 0.0026)
g3.add_edge("China", "New Zealand", weight = 0.0018)

g3.large = [(u, v) for (u, v, d) in g3.edges(data=True) if d["weight"] > 0.08]
g3.small = [(u, v) for (u, v, d) in g3.edges(data=True) if d["weight"] <= 0.08]

# positions for all nodes
pos = nx.spring_layout(g3)  

# nodes
nx.draw_networkx_nodes(g3, pos, node_size = 50)

# edges
nx.draw_networkx_edges(g3, pos, edgelist = g3.large, width=2, edge_color = "red")
nx.draw_networkx_edges(g3, pos, edgelist = g3.small, width=2, alpha=0.5, 
                       edge_color="blue")

# labels
nx.draw_networkx_labels(g3, pos, font_size=10, font_family="sans-serif")

plt.axis("off")
plt.show()


## Network Analysis
g3.degree()



### North American Network 

import networkx as nx 
import matplotlib.pyplot as plt


#weighted graph 
g4 = nx.Graph()

g4.add_edge("Brazil", "United States", weight = 0.20)
g4.add_edge("Mexico", "United States", weight = 0.14)
g4.add_edge("China", "United States", weight = 0.12)
g4.add_edge("United Kingdom", "United States", weight = 0.14)
g4.add_edge("Canada", "United States", weight = 0.12)
g4.add_edge("Japan", "United States", weight = 0.10)
g4.add_edge("France", "United States", weight = 0.07)
g4.add_edge("Chile", "United States", weight = 0.04)
g4.add_edge("Colombia", "United States",weight = 0.04)
g4.add_edge("Argentina", "United States",weight = 0.04)

g4.large = [(u, v) for (u, v, d) in g4.edges(data=True) if d["weight"] > 0.08]
g4.small = [(u, v) for (u, v, d) in g4.edges(data=True) if d["weight"] <= 0.08]

# positions for all nodes
pos = nx.spring_layout(g4)  

# nodes
nx.draw_networkx_nodes(g4, pos, node_size = 50)

# edges
nx.draw_networkx_edges(g4, pos, edgelist = g4.large, width=2, edge_color = "red")
nx.draw_networkx_edges(g4, pos, edgelist = g4.small, width=2, alpha=0.5, 
                       edge_color="blue")

# labels
nx.draw_networkx_labels(g4, pos, font_size=10, font_family="sans-serif")

plt.axis("off")
plt.show()


## Network Analysis
g4.degree()



### Middle Eastern Network 

import networkx as nx 
import matplotlib.pyplot as plt


#weighted graph 
g5 = nx.Graph()

g5.add_edge("Germany", "Turkey", weight = 0.31)
g5.add_edge("Bulgaria", "Turkey", weight = 0.17)
g5.add_edge("France", "Saudi Arabia", weight = 0.11)
g5.add_edge("Netherlands", "Turkey", weight = 0.12)
g5.add_edge("Germany", "Saudi Arabia", weight = 0.05)
g5.add_edge("Austria", "Turkey", weight = 0.06)
g5.add_edge("Germany", "Iraq", weight = 0.04)
g5.add_edge("Italy", "Saudi Arabia", weight = 0.05)
g5.add_edge("France", "Turkey", weight = 0.03)
g5.add_edge("Turkey", "United Kingdom", weight = 0.06)

g5.large = [(u, v) for (u, v, d) in g5.edges(data=True) if d["weight"] > 0.08]
g5.small = [(u, v) for (u, v, d) in g5.edges(data=True) if d["weight"] <= 0.08]

# positions for all nodes
pos = nx.spring_layout(g5)  

# nodes
nx.draw_networkx_nodes(g5, pos, node_size = 50)

# edges
nx.draw_networkx_edges(g5, pos, edgelist = g5.large, width=2, edge_color = "red")
nx.draw_networkx_edges(g5, pos, edgelist = g5.small, width=2, alpha=0.5, 
                       edge_color="blue")

# labels
nx.draw_networkx_labels(g5, pos, font_size=10, font_family="sans-serif")

plt.axis("off")
plt.show()


## Network Analysis
g5.degree()
for node in g5.nodes():
    print(node, g5.degree(node))


nx.number_connected_components(g5)
g5.comps = nx.connected_components(g5)
for c in g5.comps:
    print(len(c))
    
g5.comp = list(nx.connected_components(g5))[0]
g5.comp = nx.subgraph(g5, g5.comp)



### Latin American Network 

import networkx as nx 
import matplotlib.pyplot as plt


#weighted graph 
g6 = nx.Graph()

g6.add_edge("Brazil", "United States", weight = 0.36)
g6.add_edge("Mexico", "United States", weight = 0.24)
g6.add_edge("Chile", "United States", weight = 0.06)
g6.add_edge("Colombia", "United States", weight = 0.08)
g6.add_edge("Argentina", "United States", weight = 0.06)
g6.add_edge("Argentina", "Chile", weight = 0.05)
g6.add_edge("Argentina", "Brazil", weight = 0.04)
g6.add_edge("Peru", "United States", weight = 0.04)
g6.add_edge("Panama", "United States",weight = 0.03)
g6.add_edge("Ecuador", "United States",weight = 0.02)

g6.large = [(u, v) for (u, v, d) in g6.edges(data=True) if d["weight"] > 0.08]
g6.small = [(u, v) for (u, v, d) in g6.edges(data=True) if d["weight"] <= 0.08]

# positions for all nodes
pos = nx.spring_layout(g6)  

# nodes
nx.draw_networkx_nodes(g6, pos, node_size = 50)

# edges
nx.draw_networkx_edges(g6, pos, edgelist = g6.large, width=2, edge_color = "red")
nx.draw_networkx_edges(g6, pos, edgelist = g6.small, width=2, alpha=0.5, 
                       edge_color="blue")

# labels
nx.draw_networkx_labels(g6, pos, font_size=10, font_family="sans-serif")

plt.axis("off")
plt.show()


## Network Analysis
g6.degree()



### European Network 

import networkx as nx 
import matplotlib.pyplot as plt


#weighted graph 
g7 = nx.Graph()

g7.add_edge("Germany", "Netherlands", weight = 0.17)
g7.add_edge("France", "Germany", weight = 0.13)
g7.add_edge("Netherlands", "United Kingdom", weight = 0.13)
g7.add_edge("France", "Spain", weight = 0.10)
g7.add_edge("France", "United Kingdom", weight = 0.10)
g7.add_edge("United Kingdom", "United States", weight = 0.10)
g7.add_edge("Germany", "United Kingdom", weight = 0.08)
g7.add_edge("Germany", "Russia", weight = 0.08)
g7.add_edge("France", "Netherlands", weight = 0.06)
g7.add_edge("Austria", "Germany", weight = 0.05)

elarge = [(u, v) for (u, v, d) in g7.edges(data=True) if d["weight"] > 0.08]
esmall = [(u, v) for (u, v, d) in g7.edges(data=True) if d["weight"] <= 0.08]

# positions for all nodes
pos = nx.spring_layout(g7)  

# nodes
nx.draw_networkx_nodes(g7, pos, node_size = 50)

# edges
nx.draw_networkx_edges(g7, pos, edgelist = elarge, width=2, edge_color = "red")
nx.draw_networkx_edges(g7, pos, edgelist = esmall, width=2, alpha=0.5, 
                       edge_color="blue")

# labels
nx.draw_networkx_labels(g7, pos, font_size=10, font_family="sans-serif")

plt.axis("off")
plt.show()


## Network Analysis
g7.degree()



### International Network 

import networkx as nx 
import matplotlib.pyplot as plt


#weighted graph 
g7 = nx.Graph()

g7.add_edge("Germany", "Netherlands", weight = 0.17)
g7.add_edge("France", "Germany", weight = 0.13)
g7.add_edge("Netherlands", "United Kingdom", weight = 0.13)
g7.add_edge("France", "Spain", weight = 0.10)
g7.add_edge("France", "United Kingdom", weight = 0.10)
g7.add_edge("United Kingdom", "United States", weight = 0.10)
g7.add_edge("Germany", "United Kingdom", weight = 0.08)
g7.add_edge("Germany", "Russia", weight = 0.08)
g7.add_edge("France", "Netherlands", weight = 0.06)
g7.add_edge("Austria", "Germany", weight = 0.05)

elarge = [(u, v) for (u, v, d) in g7.edges(data=True) if d["weight"] > 0.08]
esmall = [(u, v) for (u, v, d) in g7.edges(data=True) if d["weight"] <= 0.08]

# positions for all nodes
pos = nx.spring_layout(g7)  

# nodes
nx.draw_networkx_nodes(g7, pos, node_size = 50)

# edges
nx.draw_networkx_edges(g7, pos, edgelist = elarge, width=2, edge_color = "red")
nx.draw_networkx_edges(g7, pos, edgelist = esmall, width=2, alpha=0.5, 
                       edge_color="blue")

# labels
nx.draw_networkx_labels(g7, pos, font_size=10, font_family="sans-serif")

plt.axis("off")
plt.show()





