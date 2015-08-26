##Search a 2D Matrix II
##Write an efficient algorithm that searches for a value in an m x n matrix.
##This matrix has the following properties:
##Integers in each row are sorted in ascending from left to right.
##Integers in each column are sorted in ascending from top to bottom.
##
##2015年8月23日 18:40:00  AC
##zss

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if  not matrix:return False
        index = [matrix[i][0] for i in range(len(matrix))]
        get,i = self.BS(index,0,len(index),target)
        if get:return True
        for i in range(i):
            if self.BS(matrix[i],0,len(matrix[i]),target)[0]:
                return True
        return False


    def BS(self,nums,begin,end,target):
        if begin+1>end:
            return False,begin
        mid = (end+begin)//2
        if nums[mid]==target:return True,mid
        elif nums[mid]>target:
            return self.BS(nums,begin,mid,target)
        elif nums[mid]<target:
            return self.BS(nums,mid+1,end,target)
