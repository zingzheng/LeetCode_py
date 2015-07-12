##Minimum Path Sum
##Given a m x n grid filled with non-negative numbers,
##find a path from top left to bottom right
##which minimizes the sum of all numbers along its path.
##Note: You can only move either down or right at any point in time.
##
##2015年7月7日     AC
##zss

class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        m,n=len(grid),len(grid[0])
        result = [[grid[i][j] for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    result[i][j] = grid[i][j]
                elif j==0:
                    result[i][j] += result[i-1][j]
                elif i == 0:
                    result[i][j] += result[i][j-1]
                else:
                    result[i][j] += min(result[i-1][j],result[i][j-1])
        return result[-1][-1]
