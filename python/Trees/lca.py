__author__ = 'Murtaza'

import BinaryTreeNode as tn

def lca(root,a,b):
    if root==None:
        return None
    if root.get_data()==a or root.get_data()==b:
        return root
    left=lca(root.get_left(),a,b)
    right=lca(root.get_right(),a,b)
    if left and right:
        return root
    else:
        return left if left else right

def create_tree():
    """
    Tree structure:
                5
              /   \
             3     8
            / \   /
          11  12 20
               \
               21
    :return:
    """
    A=tn.BinaryTreeNode(5)
    B=tn.BinaryTreeNode(3)
    C=tn.BinaryTreeNode(8)
    D=tn.BinaryTreeNode(11)
    E=tn.BinaryTreeNode(12)
    F=tn.BinaryTreeNode(20)
    G=tn.BinaryTreeNode(21)

    A.set_left(B)
    A.set_right(C)
    B.set_left(D)
    B.set_right(E)
    C.set_left(F)
    E.set_right(G)
    return A

root=create_tree()
res=lca(root,20,21)
print 'The least common ancestor is:',res.get_data()
