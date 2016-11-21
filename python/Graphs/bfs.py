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

def bfs(g, start):
    q = []
    print "En-Queue:",start.id
    q.insert(0,start)
    marked = [start]      # ideally this should be a variable in the class
    traversal = []

    while q:
        current = q.pop()
        print "De-Queue:",current.id
        traversal.append(current.id)
        current.visited = True
        for next in current.get_connections():
            if next not in marked and not next.visited:
                print "En-Queue:",next.id
                q.insert(0,next)
                marked.append(next)

    return traversal

def bfs_main(g):
    for v in g:
        if not v.visited:
            traversal = bfs(g,v)
    return traversal

g=create_graph()
v=g.vert_list[1]    # Getting the vertex which has key = 1
# t=bfs_main(g)   -- This can be called when you have multiple connected components
t=bfs(g,v)
print "BFS traversal:",t