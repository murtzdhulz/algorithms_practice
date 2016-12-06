__author__ = 'Murtaza'
from length_print import create_linked_list,print_list

def reverse_linked_list(head):
    prev=None
    current=head

    while current!=None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

head = create_linked_list()
print 'Before reversal:',print_list(head)
new_head=reverse_linked_list(head)
print 'After traversal:',print_list(new_head)