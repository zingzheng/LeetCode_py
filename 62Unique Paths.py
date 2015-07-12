##Unique Paths
##A robot is located at the top-left corner of a m x n grid
##(marked 'Start' in the diagram below).
##The robot can only move either down or right at any point in time.
##The robot is trying to reach the bottom-right corner of the grid
##(marked 'Finish' in the diagram below).
##How many possible unique paths are there?

##2015年7月7日  AC
##zss
##result = C((m+n-2),(m-1))

class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        a = b = 1
        for i in range(n,m+n-1):
            a *= i
        for i in range(1,m):
            b *= i
        return a//b
