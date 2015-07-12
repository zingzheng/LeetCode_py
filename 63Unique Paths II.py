##Unique Paths II
##Follow up for "Unique Paths":
##Now consider if some obstacles are added to the grids.
##How many unique paths would there be?
##An obstacle and empty space is marked as 1 and 0 respectively in the grid.


##2015年7月7日  AC
##zss

##动态规划

class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        result = [[0 for j in range(len(obstacleGrid[0]))] for i in range(len(obstacleGrid))]
        for i,row in enumerate(obstacleGrid):
            for j,n in enumerate(row):
                if n==1:
                    if i==0 and j==0:
                        return 0
                    else:
                        result[i][j] = 0   
                else:
                    if i==0 and j==0:
                        result[i][j] = 1
                    elif i==0:
                        result[i][j] = result[i][j-1]
                    elif j==0:
                        result[i][j] = result[i-1][j]
                    else:
                        result[i][j] = result[i-1][j]+result[i][j-1]
        return result[-1][-1]

