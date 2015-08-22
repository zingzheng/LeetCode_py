##Implement Trie (Prefix Tree)
##2015年8月19日 16:44:29 AC
##zss

class TrieNode:
    # Initialize your data structure here.
    def __init__(self,val):
        self.val = val
        self.isEnd = False
        self.childs = []

    def getChild(self,w):
        for child in self.childs:
            if child.val == w:
                return child
        return None
        
        

class Trie:

    def __init__(self):
        self.root = TrieNode(None)

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        if(self.search(word)):return
        node = self.root
        for i,w in enumerate(word):
            child = node.getChild(w)
            if child:
                node=child
            else:
                node.childs.append(TrieNode(w))
                node = node.getChild(w)
        node.isEnd=True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        node=self.root
        for w in word:
            tmp = node.getChild(w)
            if not tmp:
                return False
            else:
                node=tmp
        if node.isEnd:
            return True
        else:
            return False

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        node=self.root
        for w in prefix:
            tmp = node.getChild(w)
            if not tmp:
                return False
            else:
                node=tmp
        return True
        
        

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
