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

# Pass a boolean saying if the returned value is actually an ancestor or not
def lca_optimal(root,a,b):
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
    Just try doing dry run with a=11 and b=21 - It will be easy to verify
    """
    if root==None:
        return None,False

    if root.get_data()==a and root.get_data()==b:
        return root,True

    left,l_bool = lca_optimal(root.left,a,b)
    if l_bool: # we found the common ancestor
        return left,l_bool

    right,r_bool = lca_optimal(root.right,a,b)
    if r_bool: # we found the common ancestor
        return right,r_bool

    if left and right:
        return root,True
    elif root.get_data()==a or root.get_data()==b:
        # if we are at this node and in a subtree we have already found a or b then this is ancestor
        bool = True if (left or right) else False
        return root,bool
    else:
        return left if left else right, False

def lca_prints(root,a,b):
    if root==None:
        return None
    if root.get_data()==a or root.get_data()==b:
        return root
    left=lca(root.get_left(),a,b)
    if left:
        print "left is:",left.get_data()
    right=lca(root.get_right(),a,b)
    if right:
        print "right is:",right.get_data()
    if left and right:
        print "Returning from the good place:",root.get_data()
        return root
    else:
        ret = left if left else right
        if ret:
            print "Returning from here:",ret.get_data()
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
res,bool=lca_optimal(root,12,20)
if res:
    print 'The least common ancestor is:',res.get_data(),bool
else:
    print res,bool
