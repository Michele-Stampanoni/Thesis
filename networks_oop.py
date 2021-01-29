### Networks

import networkx as nx
from networkx.classes.reportviews import NodeView, EdgeView, DegreeView
from networkx.exception import NetworkXError

class Graph:
    
    node_dict_factory = dict
    node_attr_dict_factory = dict
    adjlist_outer_dict_factory = dict
    adjlist_inner_dict_factory = dict
    edge_attr_dict_factory = dict
    graph_attr_dict_factory = dict
    
    def __init__(self, input_data=None, **attr):
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
            
            
    def num_nodes(self):
        return len(self._node)
    
    def edges(self):
        return EdgeView(self)
    
    def degree(self):
        return DegreeView(self)
    
   
    

G = Graph()
asia_net = (config['asia_nodes']['3'], config['asia_nodes']['5'])
G.add_edge(*asia_net)
G.add_edges_from([(1, 2), (1, 3)])
G.add_edges_from([(config['eu_nodes']['1'], config['eu_nodes']['4']), 
                  (config['eu_nodes']['3'], config['eu_nodes']['6']),
                  (config['eu_nodes']['4'], config['eu_nodes']['7']),
                  (config['eu_nodes']['4'], config['eu_nodes']['9']),
                  (config['eu_nodes']['9'], config['northam_nodes']['2']),
                  (config['eu_nodes']['3'], config['eu_nodes']['9']),
                  (config['eu_nodes']['3'], config['eu_nodes']['8']),
                  (config['eu_nodes']['6'], config['eu_nodes']['9']),
                  (config['eu_nodes']['3'], config['eu_nodes']['4']),
                  (config['eu_nodes']['4'], config['eu_nodes']['6'])])
G.num_nodes()
edges(G)
degree(G)



    
  

    
    
    