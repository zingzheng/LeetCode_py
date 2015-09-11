##Maximal Rectangle
##Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
##
##2015年9月9日 10:20:11  AC
##zss

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m=0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j]=int(matrix[i][j])
                if i!=0 and matrix[i][j]==1:
                    matrix[i][j]+=matrix[i-1][j]
        for row in matrix:
            m=max(m,self.largestRectangleArea(row))
        return m

    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack=[]
        height.append(0)
        i=largest=0
        while i < len(height):
            if len(stack)==0 or  height[i]>height[stack[-1]]:
                stack.append(i)
                i+=1
            else:
                tmp = stack.pop(-1)
                largest = max(largest,height[tmp]*(i if len(stack)==0 else i-stack[-1]-1))
        return largest
