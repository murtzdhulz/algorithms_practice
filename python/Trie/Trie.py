__author__ = 'Murtaza'

class TrieNode:
    # c is the character that should go in this Trie node
    def __init__(self, c=None):
        # children is a dict mapping characters to the children (other trienodes)
        self.children={}
        self.char=c
        self.terminates=False

    def add_word(self,word):
        if word==None or len(word)==0:
            return

        child=self.get_child(word[0])
        if child==None:
            child=TrieNode(word[0])
            self.children[word[0]]=child

        if len(word)>1:
            child.add_word(word[1:])
        else:
            child.set_terminates(True)

    def get_child(self,c):
        return self.children.get(c)

    def get_char(self):
        return self.char

    def set_terminates(self,t):
        self.terminates=t

    def get_terminates(self):
        return self.terminates

class Trie:
    def __init__(self, word_list=None):
        self.root=TrieNode()
        if word_list!=None:
            for word in word_list:
                # print "Adding word:",word
                self.root.add_word(word)

    def insert(self,word):
        self.root.add_word(word)

    def contains(self,prefix,exact=False):
        last_node=self.root
        for i in xrange(len(prefix)):
            last_node=last_node.get_child(prefix[i])
            # print last_node,prefix[i]
            if last_node==None:
                return False
        return not exact or last_node.get_terminates()

    def get_root(self):
        return self.root

words=["hello","heaven","he"]
T=Trie(words)
print T.contains("mean")
print T.contains("hell",False)
print T.contains("hello",True)
