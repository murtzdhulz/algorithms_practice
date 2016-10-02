__author__ = 'Murtaza'

import BinaryTreeNode as tn
import Queue as qu

A=tn.BinaryTreeNode(5)
B=tn.BinaryTreeNode(3)
C=tn.BinaryTreeNode(8)
A.set_left(B)
A.set_right(C)
B.set_left(tn.BinaryTreeNode(11))
B.set_right(tn.BinaryTreeNode(12))

def level_order_traversal(root):
    if not root:
        return

    q = qu.Queue()
    q.put(root)

    while not q.empty():
        cur_node = q.get()
        print cur_node.get_data()
        if cur_node.get_left():
            q.put(cur_node.get_left())
        if cur_node.get_right():
            q.put(cur_node.get_right())

def size_of_binary_tree(root):
    if not root:
        return 0
    return size_of_binary_tree(root.get_left()) + size_of_binary_tree(root.get_right()) + 1

print 'Level order traversal of the tree is:'
level_order_traversal(A)
print '\nSize of the tree is:',size_of_binary_tree(A)