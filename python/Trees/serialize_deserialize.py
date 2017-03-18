from BinaryTreeNode import BinaryTreeNode
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        s=[]
        self.get_string_rep(root,s)
        return ",".join(s)

    def get_string_rep(self,node,s):
        if node==None:
            s.append("X")
        else:
            s.append(str(node.val))
            self.get_string_rep(node.left,s)
            self.get_string_rep(node.right,s)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        s=data.split(",")
        return self.get_tree_rep(s)

    def get_tree_rep(self,s):
        cur_val=s.pop(0)
        if cur_val=="X":
            return None
        node=BinaryTreeNode(int(cur_val))
        node.left=self.get_tree_rep(s)
        node.right=self.get_tree_rep(s)
        return node


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))__author__ = 'Murtaza'
