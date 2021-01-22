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


## Network Value
len(g1.nodes)
nvf_asia_metcalfe = len(g1.nodes)**2
nvf_asia_reed = (2**len(g1.nodes)) - 1



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


## Network Value
len(g2.nodes)
nvf_africa_metcalfe = len(g2.nodes)**2
nvf_africa_reed = (2**len(g2.nodes)) - 1



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


## Network Value
len(g3.nodes)
nvf_oceania_metcalfe = len(g3.nodes)**2
nvf_oceania_reed = (2**len(g3.nodes)) - 1



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


## Network Value
len(g4.nodes)
nvf_namerica_metcalfe = len(g4.nodes)**2
nvf_namerica_reed = (2**len(g4.nodes)) - 1



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
nx.draw_networkx_edges(g5, pos, edgelist = g5.large, width=4, edge_color = "red")
nx.draw_networkx_edges(g5, pos, edgelist = g5.small, width=2, alpha=0.5, 
                       edge_color="blue")

# labels
nx.draw_networkx_labels(g5, pos, font_size=10, font_family="sans-serif")

# plot
plt.axis("off")
plt.show()


## Network Value
len(g5.nodes)
nvf_mideast_metcalfe = len(g5.nodes)**2
nvf_mideast_reed = (2**len(g5.nodes)) - 1

 
## Network Analysis
g5.degree()
for node in g5.nodes():
    print(node, g5.degree(node))

g5.degree(weight = "weight")
g5.size(weight = "weight")



g5.add_node("Germany", status = "Vulnerable")
g5.nodes["Germany"]["status"]


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

# plot
plt.axis("off")
plt.show()


## Network Analysis
len(g6.nodes)
nvf_lamerica_metcalfe = len(g6.nodes)**2
nvf_lamerica_reed = (2**len(g6.nodes)) - 1



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

g7.large = [(u, v) for (u, v, d) in g7.edges(data=True) if d["weight"] > 0.08]
g7.small = [(u, v) for (u, v, d) in g7.edges(data=True) if d["weight"] <= 0.08]

# positions for all nodes
pos = nx.spring_layout(g7)  

# nodes
nx.draw_networkx_nodes(g7, pos, node_size = 50)

# edges
nx.draw_networkx_edges(g7, pos, edgelist = g7.large, width=2, edge_color = "red")
nx.draw_networkx_edges(g7, pos, edgelist = g7.small, width=2, alpha=0.5, 
                       edge_color="blue")

# labels
nx.draw_networkx_labels(g7, pos, font_size=10, font_family="sans-serif")

# plot
plt.axis("off")
plt.show()


## Network Value
len(g7.nodes)
nvf_europe_metcalfe = len(g7.nodes)**2
nvf_europe_reed = (2**len(g7.nodes)) - 1



### Continental Network 

import networkx as nx 
import matplotlib.pyplot as plt


#weighted graph 
g8 = nx.Graph()

g8.add_edge("Asia", "Africa", weight = 0.09)
g8.add_edge("Asia", "Europe", weight = 10.32)
g8.add_edge("Asia", "Latin America", weight = 0)
g8.add_edge("Asia", "Middle East", weight = 1.26)
g8.add_edge("Asia", "Oceania", weight = 0.77)
g8.add_edge("Europe", "Africa", weight = 5.61)
g8.add_edge("Europe", "Latin America", weight = 0.13)
g8.add_edge("Europe", "Middle East", weight = 16.61)
g8.add_edge("Europe", "Oceania", weight = 0.01)
g8.add_edge("Latin America", "Africa", weight = 0)
g8.add_edge("Latin America", "Middle East", weight = 0)
g8.add_edge("Latin America", "Oceania", weight = 0)
g8.add_edge("Middle East", "Africa", weight = 0.16)
g8.add_edge("Middle East", "Oceania", weight = 0)
g8.add_edge("Oceania", "Africa", weight = 0)
g8.add_edge("North America", "Africa", weight = 0.1)
g8.add_edge("North America", "Asia", weight = 18.00)
g8.add_edge("North America", "Europe", weight = 16.31)
g8.add_edge("North America", "Latin America", weight = 28.47)
g8.add_edge("North America", "Middle East", weight = 0.18)
g8.add_edge("North America", "Oceania", weight = 2.05)

g8.large = [(u, v) for (u, v, d) in g8.edges(data=True) if d["weight"] > 1]
g8.small = [(u, v) for (u, v, d) in g8.edges(data=True) if d["weight"] <= 1]

# positions for all nodes
pos = nx.spring_layout(g8)  

# nodes
nx.draw_networkx_nodes(g8, pos, node_size = 50)

# edges
nx.draw_networkx_edges(g8, pos, edgelist = g8.large, width=2, edge_color = "red")
nx.draw_networkx_edges(g8, pos, edgelist = g8.small, width=2, alpha=0.5, 
                       edge_color="blue")

# labels
nx.draw_networkx_labels(g8, pos, font_size=10, font_family="sans-serif")

# plot
plt.axis("off")
plt.show()


## Network Value 
len(g8.nodes)
nvf_global_metcalfe = len(g8.nodes)**2
nvf_global_reed = (2**len(g8.nodes)) - 1






