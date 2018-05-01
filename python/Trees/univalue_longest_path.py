# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def path_from_here(node):
            if not node: return 0
            left_length = path_from_here(node.left)
            right_length = path_from_here(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.val == node.left.val:
                left_arrow = left_length + 1
            if node.right and node.val == node.right.val:
                right_arrow = right_length + 1
            self.ans = max(self.ans, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        path_from_here(root)
        return self.ans

"""
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
"""
