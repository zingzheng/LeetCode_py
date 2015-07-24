##Word Search
##Given a 2D board and a word, find if the word exists in the grid.
##The word can be constructed from letters of sequentially adjacent cell,
##where "adjacent" cells are those horizontally or vertically neighboring.
##The same letter cell may not be used more than once
##
##2015年7月13   AC
##zss

class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        board = [list(board[i]) for i in range(len(board))]
        if self.reduce(board,word,-1,-1):
            return True
        else:
            return False

    def reduce(self,board,word,i,j):
        if not word:
            return True
        candidate = self.search(board,word[0],i,j)
        for i,j in candidate:
            board[i][j] = '.'
            if self.reduce(board,word[1:],i,j):
                return True
            board[i][j] = word[0]

    def search(self,board,char,i,j):
        result = []
        if i==j==-1:
            ##first search
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == char:
                        result.append((i,j))
        else:
            if i-1>=0 and board[i-1][j] == char:
                result.append((i-1,j))
            if j-1>=0 and board[i][j-1] == char:
                result.append((i,j-1))
            if i+1<=len(board)-1 and board[i+1][j] == char:
                result.append((i+1,j))
            if j+1<=len(board[0])-1 and board[i][j+1] == char:
                result.append((i,j+1))
        return result
