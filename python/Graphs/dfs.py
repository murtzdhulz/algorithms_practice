from graph import Vertex, Graph

def create_graph():
    g = Graph()
    g.add_edge(1,2)
    g.add_edge(1,3)
    g.add_edge(2,3)
    g.add_edge(3,4)
    g.add_edge(4,2)
    g.add_edge(2,5)
    return g

def print_test(g):
    # start processing the veritices
    for e in g:
        print type(e),isinstance(e,Vertex),e.id, e.get_connections()
        print e

def dfs(g):
    for e in g:
        if not e.visited:
            print "In DFS", e.id
            explore(e)

def explore(v):
    v.visited = True
    print v.id
    neighbors = v.get_connections()
    for a in neighbors:
        if not a.visited:
            print "In Explore", a.id
            explore(a)

g=create_graph()
dfs(g)
