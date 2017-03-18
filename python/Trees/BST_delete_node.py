__author__ = 'Murtaza'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root==None:
            return None

        if key<root.val:
            root.left=self.deleteNode(root.left,key)
        elif key>root.val:
            root.right=self.deleteNode(root.right,key)
        else:
            if root.left==None:
                return root.right
            elif root.right==None:
                return root.left
            else:
                min_node=self.find_min(root.right)
                root.val=min_node.val
                root.right=self.deleteNode(root.right,min_node.val)
        return root

    def find_min(self, node):
        if node==None:
            return None
        while node.left:
            node=node.left
        return node