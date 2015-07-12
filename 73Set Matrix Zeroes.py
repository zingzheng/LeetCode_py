##Set Matrix Zeroes
##Given a m x n matrix, if an element is 0, set its entire row and column to 0.
##Do it in place.
##
##2015年7月12日   AC
##zss

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        row0 = cel0 = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i == 0:
                        row0 = True
                    if j == 0:
                        cel0 = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1,len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1,len(matrix[0])):
                    matrix[i][j] = 0
        for j in range(1,len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(1,len(matrix)):
                    matrix[i][j] = 0
        if row0:
            for j in range(1,len(matrix[0])):
                matrix[0][j] = 0
        if cel0:
            for i in range(1,len(matrix)):
                matrix[i][0] = 0
            
                    
