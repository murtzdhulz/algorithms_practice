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

def get_length(head):
    count=0
    cur_node=head
    while cur_node!=None:
        count+=1
        cur_node = cur_node.next
    return count

def print_list(head):
    res=""
    while head!=None:
        res+=str(head.data)+'->'
        head=head.next
    return res.rstrip('->')

# head = create_linked_list()
# print get_length(head)
# print print_list(head)