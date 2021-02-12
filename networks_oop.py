### Networks

import networkx as nx
from networkx.classes.reportviews import NodeView, EdgeView, DegreeView
from networkx.exception import NetworkXError
import networkx.convert as convert
from dataclasses import dataclass
import excel_data 
import config_parser


class Graph:
    
    node_dict_factory = dict
    node_attr_dict_factory = dict
    adjlist_outer_dict_factory = dict
    adjlist_inner_dict_factory = dict
    edge_attr_dict_factory = dict
    graph_attr_dict_factory = dict
    
    def __init__(self, input_data = None, **attr):
         self.graph_attr_dict_factory = self.graph_attr_dict_factory
         self.node_dict_factory = self.node_dict_factory
         self.node_attr_dict_factory = self.node_attr_dict_factory
         self.adjlist_outer_dict_factory = self.adjlist_outer_dict_factory
         self.adjlist_inner_dict_factory = self.adjlist_inner_dict_factory
         self.edge_attr_dict_factory = self.edge_attr_dict_factory
         self.graph = self.graph_attr_dict_factory()  # dictionary for graph attributes
         self._node = self.node_dict_factory()  # empty node attribute dict
         self._adj = self.adjlist_outer_dict_factory()  # empty adjacency dict
         
         if input_data is not None:
             convert.to_networkx_graph(input_data, create_using=self)
        # load graph attributes (must be after convert)
         self.graph.update(attr)
         
    #Adds a single edge
    def add_edge(self, u_of_edge, v_of_edge, **attr):
        u, v = u_of_edge, v_of_edge
        
        if u not in self._node:
            self._adj[u] = self.adjlist_inner_dict_factory()
            self._node[u] = self.node_attr_dict_factory()
        if v not in self._node:
            self._adj[v] = self.adjlist_inner_dict_factory()
            self._node[v] = self.node_attr_dict_factory()
        
        datadict = self._adj[u].get(v, self.edge_attr_dict_factory())
        datadict.update(attr)
        self._adj[u][v] = datadict
        self._adj[v][u] = datadict
        
    #Adds multiple edges   
    def add_edges_from(self, ebunch_to_add, **attr):
        
        
        for e in ebunch_to_add:
            ne = len(e)
            if ne == 3:
                u, v, dd = e
            elif ne == 2:
                u, v = e
                dd = {}  
            else:
                raise NetworkXError(f"Edge tuple {e} must be a 2-tuple or 3-tuple.")
            if u not in self._node:
                self._adj[u] = self.adjlist_inner_dict_factory()
                self._node[u] = self.node_attr_dict_factory()
            if v not in self._node:
                self._adj[v] = self.adjlist_inner_dict_factory()
                self._node[v] = self.node_attr_dict_factory()
            datadict = self._adj[u].get(v, self.edge_attr_dict_factory())
            datadict.update(attr)
            datadict.update(dd)
            self._adj[u][v] = datadict
            self._adj[v][u] = datadict
            
    #Returns the number of nodes in the network
    def num_nodes(self):
        return len(self._node)
    
    #Returns the edges between all the nodes
    def edges(self):
        return EdgeView(self)
    
    #Reutrns the cardinality / number of edges of each node
    def degree(self):
        return DegreeView(self)
    
    #Network value function based on Metcalfe's law: n^2 
    def nvf_met(self):
        return len(self._node)**2
    
    #Network value function based on Reed's law: 2^n 
    def nvf_reed(self):
        return 2**len(self._node)
    
    
    
### European Network using TG Data imported using pandas as a dataframe  
G = Graph()
G.add_edges_from([(eval("str(edges_eu().loc[[0], 'Node1'])[5:12]"),
                   eval("str(edges_eu().loc[[0], 'Node2'])[5:16]")),
                  (eval("str(edges_eu().loc[[1], 'Node1'])[5:11]"),
                   eval("str(edges_eu().loc[[1], 'Node2'])[5:12]")),
                  (eval("str(edges_eu().loc[[2], 'Node1'])[5:16]"),
                   eval("str(edges_eu().loc[[2], 'Node2'])[5:19]")),
                  (eval("str(edges_eu().loc[[3], 'Node1'])[5:11]"), 
                   eval("str(edges_eu().loc[[3], 'Node2'])[5:10]")), 
                  (eval("str(edges_eu().loc[[4], 'Node1'])[5:11]"),  
                   eval("str(edges_eu().loc[[4], 'Node2'])[5:19]")),
                  (eval("str(edges_eu().loc[[5], 'Node1'])[5:19]"),
                   eval("str(edges_eu().loc[[5], 'Node2'])[5:18]")), 
                  (eval("str(edges_eu().loc[[6], 'Node1'])[5:12]"),
                   eval("str(edges_eu().loc[[6], 'Node2'])[5:19]")),
                  (eval("str(edges_eu().loc[[7], 'Node1'])[5:12]"),
                   eval("str(edges_eu().loc[[7], 'Node2'])[5:11]")), 
                  (eval("str(edges_eu().loc[[8], 'Node1'])[5:11]"),
                   eval("str(edges_eu().loc[[8], 'Node2'])[5:16]")),
                  (eval("str(edges_eu().loc[[9], 'Node1'])[5:12]"),
                   eval("str(edges_eu().loc[[9], 'Node2'])[5:12]"))])

G.num_nodes()
edges(G)
degree(G)
G.nvf_met() 
G.nvf_reed() 



### European Network using TG Data from config file 
""" This mmethod uses the data from the config file,
but the config function is not defined"""  

G1 = Graph()
G1.add_edges_from([(config['eu_nodes']['1'], config['eu_nodes']['4']), 
                  (config['eu_nodes']['3'], config['eu_nodes']['6']),
                  (config['eu_nodes']['4'], config['eu_nodes']['7']),
                  (config['eu_nodes']['4'], config['eu_nodes']['9']),
                  (config['eu_nodes']['9'], config['northam_nodes']['2']),
                  (config['eu_nodes']['3'], config['eu_nodes']['9']),
                  (config['eu_nodes']['3'], config['eu_nodes']['8']),
                  (config['eu_nodes']['6'], config['eu_nodes']['9']),
                  (config['eu_nodes']['3'], config['eu_nodes']['4']),
                  (config['eu_nodes']['4'], config['eu_nodes']['6'])])
G1.num_nodes()
edges(G1)
degree(G1)
G1.nvf_met() 
G1.nvf_reed() 




    
    

