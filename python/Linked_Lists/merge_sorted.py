__author__ = 'Murtaza'
from Node import Node
from LL_helpers import print_list,create_list

def merge_sorted(L1,L2):
    head = Node(float('inf'))
    pointer = head

    while(True):
        if L1==None:
            pointer.next=L2
            break
        elif L2==None:
            pointer.next=L1
            break
        else:
            if L1.get_data()<=L2.get_data():
                pointer.next=L1
                L1=L1.next
            else:
                pointer.next=L2
                L2=L2.next
            pointer=pointer.next

    return head.next

def merge_sorted_2(L1,L2):
    head = None
    pointer = head

    while(True):
        if L1==None:
            if pointer==None:
                head=L2
            else:
                pointer.next=L2
            break
        elif L2==None:
            if pointer==None:
                head=L1
            else:
                pointer.next=L1
            break
        else:
            if L1.get_data()<=L2.get_data():
                if pointer==None:
                    pointer=L1
                    head=pointer
                    L1=L1.next
                    continue
                else:
                    pointer.next=L1
                    L1=L1.next
            else:
                if pointer==None:
                    pointer=L2
                    head=pointer
                    L2=L2.next
                    continue
                else:
                    pointer.next=L2
                    L2=L2.next
            pointer=pointer.next

    return head

L1 = create_list([2,7,13,15,21])
L2 = create_list([1,5,18,52,53])
print print_list(merge_sorted_2(L1,L2))

# Trial Code
# def merge_sorted_2(L1,L2):
#     head = None
#     pointer = head
#
#     while(True):
#         print "Here",L1.get_data(),L2.get_data()
#         if L1==None:
#             if pointer==None:
#                 head=L2
#             else:
#                 pointer.next=L2
#             break
#         elif L2==None:
#             if pointer==None:
#                 head=L1
#             else:
#                 pointer.next=L1
#             break
#         else:
#             if L1.get_data()<=L2.get_data():
#                 if pointer==None:
#                     pointer=L1
#                     head=pointer
#                 else:
#                     print "Pointer in L1 less is",pointer.data
#                     pointer.next=L1
#                 L1=L1.next
#             else:
#                 if pointer==None:
#                     pointer=L2
#                     head=pointer
#                 else:
#                     print "Pointer in L2 less is",pointer.data
#                     pointer.next=L2
#                 L2=L2.next
#             pointer=pointer.next
#
#     return head