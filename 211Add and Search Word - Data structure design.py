##Add and Search Word - Data structure design
##2015年6月14日   TLE
##zss

##child-bro-tree TLE
##class treeNode:
##    def __init__(self,val):
##        self.val = val
##        self.child = None
##        self.bro = None
##
##class WordDictionary:
##
##    # initialize your data structure here.
##    def __init__(self):
##        self.root = treeNode(None)
##        
##    def iterChild(self,root):
##        childs = []
##        node = root.child
##        while node:
##            childs.append(node)
##            node = node.bro
##        return childs
##
##    def Add(self,root,char):
##        childs = self.iterChild(root)
##        #不存在子
##        if not childs:
##            newNode = treeNode(char)
##            root.child = newNode
##            return newNode
##        #子中存在该字母
##        for node in childs:
##            if node.val == char:
##                return node
##        #子中不存在该字母
##        newNode = treeNode(char)
##        childs[-1].bro = newNode
##        return newNode
##
##    def searchWord(self,root,word):
##        childs = self.iterChild(root)
##        if not childs:
##            return False
##        for child in childs:
##            if child.val == word[0] or word[0] == '.':
##                if len(word) == 1:
##                    return True
##                else:
##                    return self.searchWord(child,word[1:])
##        return False
##
##      
##    # @param {string} word
##    # @return {void}
##    # Adds a word into the data structure.
##    def addWord(self, word):
##        r = self.root
##        for w in word:
##            r = self.Add(r,w)
##            
##
##    # @param {string} word
##    # @return {boolean}
##    # Returns if the word is in the data structure. A word could
##    # contain the dot character '.' to represent any one letter.
##    def search(self, word):
##        return self.searchWord(self.root,word)
        

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")



class WordDictionary:

    # initialize your data structure here.
    def __init__(self):
        self.wordDic = {}
        
    
    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        if len(word) in self.wordDic:
            self.wordDic[len(word)].append(word)
        else:
            self.wordDic[len(word)] = [word]
        
            

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        if len(word) not in self.wordDic:
            return False
        for w in self.wordDic[len(word)]:
            flag = 1
            for i in range(len(word)):
                if word[i] == '.' or word[i] == w[i]:
                    continue
                else:
                    flag = 0
                    break
            if flag == 1:
                return True
        return False
            
                    
        
