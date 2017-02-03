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

def path_exists(g,start,end):
    if start==end:
        return True, [start]

    #put initialisation of state to 0

    start.state = 1 # Processing
    q = [start]

    while len(q)!=0:
        cur_vertex = q.pop()
        for v in cur_vertex.get_connections():
            if v==end:
                return True
            else:
                if v.state==0:     # This check could be kept on the top
                    v.state=1
                    q.insert(0,v)
    return False

def path_with_length(g,start,end):
    if start==end:
        return True, [start]

    #put initialisation of state to 0

    start.state = 1 # Processing
    q = [(start,0)]

    while len(q)!=0:
        cur_vertex, cur_dist = q.pop()
        for v in cur_vertex.get_connections():
            if v==end:
                return True,(cur_dist+1)            # Since we terminate the moment we see the goal, without adding to the couter
            else:
                if v.state==0:     # This check could be kept on the top
                    v.state=1
                    q.insert(0,(v,cur_dist+1))
    return False

g=create_graph()
v=g.vert_list[1]    # Getting the vertex which has key = 1
u=g.vert_list[4]
# g.add_vertex(5)
# u=g.vert_list[5]
print path_with_length(g,v,u)