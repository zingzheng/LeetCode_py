##Search a 2D Matrix
##Write an efficient algorithm that searches for a value in an m x n matrix.
##This matrix has the following properties:
##Integers in each row are sorted from left to right.
##The first integer of each row is greater than the last integer
##of the previous row.

##2015年7月12日  AC
##zss

class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        row = self.binaryRows(matrix,0,len(matrix)-1,target)
        if not row:
            return False
        else:
            return self.binaryInRow(row,0,len(row)-1,target)


    # find out which row may be fit
    # return a[i] which a[i][0]<=target and a[i+1][0]> target 
    def binaryRows(self,matrix,i,j,target):
        if not matrix or matrix[i][0]> target or i > j:
            return None
        mid = (i+j)//2
        if matrix[mid][0] == target:
            return matrix[mid]
        elif matrix[mid][0]< target:
            if mid+1 < len(matrix):
                if matrix[mid+1][0]>target:
                    return matrix[mid]
                else:
                    return self.binaryRows(matrix,mid+1,j,target)
            else:
                return matrix[mid]
        elif matrix[mid][0]> target:
            return self.binaryRows(matrix,i,mid-1,target)

    def binaryInRow(self,row,i,j,target):
        if not row or row[i]>target or row[j]<target or i>j:
            return False
        mid = (i+j)//2
        if row[mid] == target:
            return True
        elif row[mid] < target:
            return self.binaryInRow(row,mid+1,j,target)
        else:
            return self.binaryInRow(row,i,mid-1,target)
