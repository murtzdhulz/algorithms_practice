__author__ = 'Murtaza'

import BinaryTreeNode as tn
import Queue as qu

def number_of_leaves(root):
    if root==None:
        return 0
    q=qu.Queue()
    q.put(root)
    count=0
    while not q.empty():
        # print 'Going in'
        node=q.get()
        if node.get_left() == None and node.get_right() == None:
            # print 'found count'
            count+=1
        else:
            if node.get_left():
                # print 'go left'
                q.put(node.get_left())
            if node.get_right():
                # print 'go right'
                q.put(node.get_right())
    return count

def create_tree():
    """
    Tree structure:
                5
              /   \
             3     8
            / \
          11  12
    :return:
    """
    A=tn.BinaryTreeNode(5)
    B=tn.BinaryTreeNode(3)
    C=tn.BinaryTreeNode(8)
    A.set_left(B)
    A.set_right(C)
    B.set_left(tn.BinaryTreeNode(11))
    B.set_right(tn.BinaryTreeNode(12))
    return A

root=create_tree()
print 'The number of leaves are:',number_of_leaves(root)


