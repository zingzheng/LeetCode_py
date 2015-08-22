##Surrounded Regions
##Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.
##A region is captured by flipping all 'O's into 'X's in that surrounded region.
##
##2015年8月17日 09:35:16   AC
##zss

class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solve(self, board):
        if not board or len(board)<3 or len(board[0])<3:return
        for i,row in enumerate(board):
            board[i] = list(row)
        maxi,maxj = len(board)-1,len(board[0])-1
        for j in range(maxj+1):
            if board[0][j]=='O':self.DFS(board,0,j)
            if board[maxi][j]=='O':self.DFS(board,maxi,j)
        for i in range(1,maxi):
            if board[i][0]=='O':self.DFS(board,i,0)
            if board[i][maxj]=='O':self.DFS(board,i,maxj)
        for i in range(maxi+1):
            for j in range(maxj+1):
                if board[i][j]=='O':board[i][j]='X'
                if board[i][j]=='#':board[i][j]='O'
        
    ##RuntimeError: maximum recursion depth exceeded in cmp
##    def DFS(self,board,i,j):
##        board[i][j] = '#'
##        if i-1>=0 and board[i-1][j]=='O':self.DFS(board,i-1,j)
##        if i+1<len(board) and board[i+1][j]=='O':self.DFS(board,i+1,j)
##        if j-1>=0 and board[i][j-1]=='O':self.DFS(board,i,j-1)
##        if j+1<len(board[0]) and board[i][j+1]=='O':self.DFS(board,i,j+1)

    def DFS(self,board,x,y):
        stack=[[x,y]]
        while stack:
            i,j = stack.pop(-1)
            board[i][j] = '#'
            if i-1>=0 and board[i-1][j]=='O':stack.append([i-1,j])
            if i+1<len(board) and board[i+1][j]=='O':stack.append([i+1,j])
            if j-1>=0 and board[i][j-1]=='O':stack.append([i,j-1])
            if j+1<len(board[0]) and board[i][j+1]=='O':stack.append([i,j+1])
            
    
        
