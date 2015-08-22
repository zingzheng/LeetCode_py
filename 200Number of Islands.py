##Number of Islands
##Given a 2d grid map of '1's (land) and '0's (water),count the number of islands.
##An island is surrounded by water and is formed by connecting adjacent lands
##horizontally or vertically.
##You may assume all four edges of the grid are all surrounded by water.

##2015年8月19日 15:06:32 AC
##zss

class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        count=0
        for i,row in enumerate(grid):
            grid[i] = list(row)
        for x,row in enumerate(grid):
            for y,char in enumerate(row):
                if char=='1':
                    count+=1
                    self.DFS(grid,x,y)
        return count


    def DFS(self,board,x,y):
        stack=[[x,y]]
        while stack:
            i,j = stack.pop(-1)
            board[i][j] = '0'
            if i-1>=0 and board[i-1][j]=='1':stack.append([i-1,j])
            if i+1<len(board) and board[i+1][j]=='1':stack.append([i+1,j])
            if j-1>=0 and board[i][j-1]=='1':stack.append([i,j-1])
            if j+1<len(board[0]) and board[i][j+1]=='1':stack.append([i,j+1])
