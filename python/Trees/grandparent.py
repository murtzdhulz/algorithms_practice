__author__ = 'Murtaza'
import BinaryTreeNode as tn

def create_tree():
    """
    Tree structure:
                5
              /   \
             3     8
            / \
          11  12
              /
            13
    :return:
    """
    A=tn.BinaryTreeNode(5)
    B=tn.BinaryTreeNode(3)
    C=tn.BinaryTreeNode(8)
    D=tn.BinaryTreeNode(11)
    E=tn.BinaryTreeNode(12)
    F=tn.BinaryTreeNode(13)
    A.set_left(B)
    A.set_right(C)
    B.set_left(D)
    B.set_right(E)
    E.set_left(F)
    return A

def grandparent(root,key):
    print root.data
    if root==None:
        return

    if root.left!=None:
        if (root.left.left!=None and root.left.left.data==key) or (root.left.right!=None and root.left.right.data==key):
            return root
        else:
            left=grandparent(root.left,key)
            if left!=None:
                return left

    if root.right!=None:
        if (root.right.left!=None and root.right.left.data==key) or (root.right.right!=None or root.right.right.data==key):
            return root
        else:
            return grandparent(root.right,key)

root=create_tree()
print grandparent(root,13).data

