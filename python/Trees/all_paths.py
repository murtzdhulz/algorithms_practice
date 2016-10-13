__author__ = 'Murtaza'

import BinaryTreeNode as tn

def print_all_paths(root,path):
    if root==None:
        return

    path.append(str(root.get_data()))

    if root.get_left() == None and root.get_right() == None:
        print '-'.join(path)
    else:
        if root.get_left()!=None:
            print_all_paths(root.get_left(),path)
            path.pop()
        if root.get_right()!=None:
            print_all_paths(root.get_right(),path)
            path.pop()

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
    D=tn.BinaryTreeNode(11)
    E=tn.BinaryTreeNode(12)
    A.set_left(B)
    A.set_right(C)
    B.set_left(D)
    B.set_right(E)
    return A

root=create_tree()
print_all_paths(root,[])

