##N-Queens II
##
##2015年7月6日   AC
##zss

class Solution:
    # @param {integer} n
    # @return {integer}
    def totalNQueens(self, n):
        self.result = 0
        self.putQueens([0]*n,0,n)
        return self.result
        
    def putQueens(self,board,index,n):
        if index == len(board):
            self.result += 1
        else:
            for i in range(n):
                if self.clashTest(board,index,i):
                    board[index]=i
                    self.putQueens(board,index+1,n)
                
    def clashTest(self,board,index,pos):
        for i in range(index):
            if board[i] == pos:
                return False
            if index-i == abs(pos-board[i]):
                return False
        return True
