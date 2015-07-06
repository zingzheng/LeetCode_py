##N-Queens
##
##2015年7月6日   AC
##zss

class Solution:
    # @param {integer} n
    # @return {string[][]}
    def solveNQueens(self, n):
        self.result = []
        self.putQueens([0]*n,0,n)
        return self.result
        
    def putQueens(self,board,index,n):
        if index == len(board):
            res = []
            for i in range(n):
                row = ['.']*n
                row[board[i]]='Q'
                res.append(''.join(row))
            self.result.append(res)
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
