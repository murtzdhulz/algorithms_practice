__author__ = 'Murtaza'

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.n=None

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        # We will find the length of the list and pass that too
        l=0
        node=head
        self.n=head
        while node:
            l+=1
            node=node.next

        root=self.get_bst(0,l-1)
        return root

    def get_bst(self, start, end):
        if start>end:
            return None

        mid=start+(end-start)/2
        left=self.get_bst(start, mid-1)
        parent=TreeNode(self.n.val)
        parent.left=left
        self.n=self.n.next
        parent.right=self.get_bst(mid+1,end)
        return parent