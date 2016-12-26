__author__ = 'Murtaza'
from Node import Node

# Takes a list as input and creates a linked list from it
def create_list(l):
    res=None
    head=None

    for val in l:
        new_node = Node(val)
        if res==None:
            res=new_node
            head=res
        else:
            res.next=new_node
            res=res.next
    return head

def print_list(head):
    res=""
    while head!=None:
        res+=str(head.data)+'->'
        head=head.next
    return res.rstrip('->')

def get_length(head):
    count=0
    cur_node=head
    while cur_node!=None:
        count+=1
        cur_node = cur_node.next
    return count

# print print_list(create_list([1,2,3]))

