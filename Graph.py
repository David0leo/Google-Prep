class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbors = {}
    
    def add_neighbor(self, vertex, edge_weight=0):
        self.neighbors[vertex] = edge_weight
    
    def get_neighbors(self):
        return self.neighbors.keys()
    
    def get_key(self):
        return self.key
    
    def get_edge_weight(self, adj_vertex):
        return self.neighbors[adj_vertex]
    
    def __str__(self):
        return str(self.key) + ' with neighbors: ' + str([v.key for key in self.neighbors])

class Graph:
    def __init__(self, directed=False):
        self.vertices = {}
        self.order = 0
        self.directed = directed
    
    def add_vertex(self, key):
        """Adds a new vertex to graph, returns the added vertex"""
        self.order += 1
        v = Vertex(key)
        self.vertices[key] = v
        return v
    
    def get_vertex(self, v):
        """Return vertex v if in vertices, or returns None"""
        return self.vertices.get(v)
    
    def add_edge(self, v, u, weight=0):
        if v not in self.vertices:
            self.add_vertex(v)
        if u not in self.vertices:
            self.add_vertex(u)
        self.vertices[v].add_neighbor(self.vertices[u], weight)
        if not self.directed:
            self.vertices[u].add_neighbor(self.vertices[u], weight)
    
    def get_vertices(self):
        return self.vertices.keys()
    
    def __contains__(self, v):
        return v in self.vertices
    
    def __iter__(self):
        return iter(self.vertices.values())