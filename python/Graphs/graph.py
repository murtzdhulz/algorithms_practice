class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}
        self.visited = False
        # Will be used in some scenarios 0-univisited, 1-processing, 2-processed
        self.state=0

    def add_neighbor(self,nbr,weight=0):
        self.connected_to[nbr] = weight

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self,nbr):
        return self.connected_to[nbr]

    def __str__(self):
        return str(self.id) + ' connected to: ' + str([x.id for x in self.connected_to])

class Graph:
    """
    The structure is:
    Graph consists of a dictionary of keys (integer values)
    Each key maps to a Vertex object
    Vertex object has a connected_to dictionary which has keys as other Vertex objects and vale as the weight measure
    """

    def __init__(self):
        self.vert_list={}
        self.num_vertices=0

    def add_vertex(self,key):
        self.num_vertices += 1
        nv = Vertex(key)
        self.vert_list[key]=nv
        return nv

    def add_edge(self, f, t, weight=0):
        if f not in self.vert_list:
            nv = self.add_vertex(f)
        if t not in self.vert_list:
            nv = self.add_vertex(t)
        self.vert_list[f].add_neighbor(self.vert_list[t], weight)

    def __contains__(self, item):
        return item in self.vert_list

    def get_vertices(self):
        return self.vert_list.keys()

    def __iter__(self):
        return iter(self.vert_list.values())
