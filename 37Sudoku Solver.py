##Sudoku Solver
##
##2015年7月2日  AC
##zss


class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solveSudoku(self, board):
        b = [[board[i][j] for j in range(9)] for i in range(9)]
        for i in range(9):
            board[i]=b[i]
        self.traceBack(board)
        ##return board
        
        

    def traceBack(self,board):
        ##board = board0.copy()
        for i,row in enumerate(board):
            for j,cell in enumerate(row):
                if cell == '.':
                    for test in range(1,10):
                        if self.crashTest(board,i,j,str(test)):
                            board[i][j] = str(test)
                            if (self.traceBack(board)):
                                return board
                            board[i][j] = '.'
                    return
                if i==8 and j==8:
                    return board


    def crashTest(self,board,i,j,test):
        if board[i].count(test)>0:
            return False
        if [board[it][j] for it in range(9)].count(test)>0:
            return False
        i,j = i//3*3,j//3*3
        if [board[i+n][j+m] for n in range(3) for m in range(3)].count(test)>0:
            return False
        return True
        
        
