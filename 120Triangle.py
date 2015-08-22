##Triangle
##Given a triangle, find the minimum path sum from top to bottom.
##Each step you may move to adjacent numbers on the row below.
##
##2015年8月14日 14:38:31 AC
##zss

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        for r in range(len(triangle)-2,-1,-1):
            for i in range(0,len(triangle[r])):
                triangle[r][i] += min(triangle[r+1][i],triangle[r+1][i+1])
        return triangle[0][0]
            
