__author__ = 'Murtaza'
from Node import Node

def create_linked_list():
    A = Node(1)
    B = Node(2)
    C = Node(3)
    D = Node(4)
    E = Node(5)

    A.set_next(B)
    B.set_next(C)
    C.set_next(D)
    D.set_next(E)

    return A

def k_element(head, k):
    p1 = head
    p2 = head

    # put p2 k steps ahead
    for i in xrange(k):
        if p2==None:
            print "Went out of bounds"
            return None
        else:
            p2=p2.next

    while p2!=None:
        p1=p1.next
        p2=p2.next

    return p1

head = create_linked_list()
print k_element(head,3).get_data()