# Serialize and deserialize an N-Ary tree

# Root is the root node and s is a char array (or list of Strings)
def serialize(root,s):
    if root!=None:
        s.append('(')
        s.append(root.val)
        for child in root.children:
            serialize(child,s)
        s.append(')')
    return ''.join(s)

def deserialize(s):
    if len(s)>0:
        if s[0]=='(':
            s.pop()
            node=TreeNode(s.pop())
            while s[0]!=')':
                node.add(deserialize(s))
            s.pop()
            return node
    return None