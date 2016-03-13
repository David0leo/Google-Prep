import Graph

g = Graph.Graph(directed=True)
for i in range(6):
    g.add_vertex(i)
print(g.vertices)
g.add_edge(0,1,5)
g.add_edge(0,5,2)
g.add_edge(1,2,4)
g.add_edge(2,3,9)
g.add_edge(3,4,7)
g.add_edge(3,5,3)
g.add_edge(4,0,1)
g.add_edge(5,4,8)
g.add_edge(5,2,1)

for v in g:
    for w in v.get_neighbors():
        print("(%s, %s)" %(v.get_key(), w.get_key()))