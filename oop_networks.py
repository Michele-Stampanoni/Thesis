

class Graph(nx.Graph):
    
    node_dict_factory = dict
    node_attr_dict_factory = dict
    adjlist_outer_dict_factory = dict
    adjlist_inner_dict_factory = dict
    edge_attr_dict_factory = dict
    graph_attr_dict_factory = dict


    def __init__(self, incoming_graph_data, **attr):
        
        self.graph_attr_dict_factory = self.graph_attr_dict_factory
        self.node_dict_factory = self.node_dict_factory
        self.node_attr_dict_factory = self.node_attr_dict_factory
        self.adjlist_outer_dict_factory = self.adjlist_outer_dict_factory
        self.adjlist_inner_dict_factory = self.adjlist_inner_dict_factory
        self.edge_attr_dict_factory = self.edge_attr_dict_factory    
        
        self.graph = self.graph_attr_dict_factory()  # dictionary for graph attributes
        self._node = self.node_dict_factory()  # empty node attribute dict
        self._adj = self.adjlist_outer_dict_factory()  # empty adjacency dict
        # attempt to load graph with data
        if incoming_graph_data is not None:
            convert.to_networkx_graph(incoming_graph_data, create_using=self)
        # load graph attributes (must be after convert)
        self.graph.update(attr)
        
    def __len__(self):
        return len(self._node)
    
    d
   
e = [(conf['num_nodes']['africa'], conf['num_nodes']['europe']), (2, 3), (3, 4)]  # list of edges
G = nx.Graph(e)

# Arbitrary graph attribute pairs (key=value) may be assigne
G = nx.Graph(e, region = "World")
G.graph





        
class Network:
        def add_node(self, node_for_adding, **attr):
            if node_for_adding not in self._node:
                self._adj[node_for_adding] = self.adjlist_inner_dict_factory()
                attr_dict = self._node[node_for_adding] = self.node_attr_dict_factory()
                attr_dict.update(attr)
            else self._node[node_for_adding].update(attr) # update attr even if node already exists


          
K3 = nx.Graph([(0, 1), (1, 2), (2, 0)])
G.add_node(K3)
n = Network()
n.add_node(0, name = "France")



