##Word Search II
##Given a 2D board and a list of words from the dictionary, find all words in the board.
##Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
##
##2015年10月25日 17:54:20
##zss

##这道题和I的最大区别在于，输入是多个word，若words规模很大，多次去使用I的递归会有很多重复操作（如共同前缀），
##因此用一个字典树存储words，对字典树进行dfs，利用board对字典树剪枝

class TrieNode:
    def __init__(self):
        self.childs = dict()
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        node = self.root
        for letter in word:
            child = node.childs.get(letter)
            if not child:
                child = TrieNode()
                node.childs[letter] = child
            node = child
        node.isWord = True

    def delete(self,word):
        node = self.root
        queue = []
        for letter in word:
            queue.append((letter,node))
            child = node.childs.get(letter)
            if not child:
                return False
            node = child
        if not node.isWord:
            return False
        if len(node.childs):
            node.isWord = False
        else:
            for letter,node in queue[::-1]:
                del node.childs[letter]
                if len(node.childs) or node.isWord:
                    break
        return True


class Solution:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def findWords(self, board, words):
        w, h = len(board[0]), len(board)
        trie = Trie()
        for word in words:
            trie.insert(word)

        visited = [[False for j in range(w)] for i in range(h)]
        dz = zip([1, 0, -1, 0], [0, 1, 0, -1])
        ans = []

        def dfs(word, node, x, y):
            node = node.childs.get(board[x][y])
            if node is None:
                return
            visited[x][y] = True
            for z in dz:
                nx, ny = x + z[0], y + z[1]
                if nx >= 0 and nx < h and ny >= 0 and ny < w and not visited[nx][ny]:
                    dfs(word + board[nx][ny], node, nx, ny)
            if node.isWord:
                ans.append(word)
                trie.delete(word)
            visited[x][y] = False

        for x in range(h):
            for y in range(w):
                dfs(board[x][y], trie.root, x, y)

        return sorted(ans)
    
