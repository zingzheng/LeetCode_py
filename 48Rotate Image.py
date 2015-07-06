##Rotate Image
##You are given an n x n 2D matrix representing an image.
##Rotate the image by 90 degrees (clockwise).
##Follow up:
##Could you do this in-place?
##
##2015年7月6   AC
##zss

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        tmp = [[matrix[i][j] for i in range(len(matrix)-1,-1,-1)] for j in range(len(matrix))]
        for i in range(len(matrix)):
            matrix[i]=tmp[i]
