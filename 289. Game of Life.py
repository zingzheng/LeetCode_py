class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        n,m=len(board),len(board[0])
        for i in range(n):
            for j in range(m):
                count=0
                for ii in (-1,0,1):
                    for jj in (-1,0,1):  
                        if 0<=i+ii<n and 0<=j+jj<m:
                            if board[i+ii][j+jj]>0:
                                count+=1
                board[i][j]=count if board[i][j]>0 else 0-count

        for i in range(n):
            for j in range(m):
                if board[i][j] in (1,2):
                    board[i][j]=0
                elif board[i][j] in (3,4):
                    board[i][j]=1
                elif board[i][j]>4:
                    board[i][j]=0
                elif board[i][j]==-3:
                    board[i][j]=1
                else:
                    board[i][j]=0

    
