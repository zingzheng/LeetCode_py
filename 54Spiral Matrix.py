##Spiral Matrix
##Given a matrix of m x n elements (m rows, n columns)
##return all elements of the matrix in spiral order.
##
##2015年7月6日  AC
##zss

class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        result = []
        while matrix:
            for i in range(len(matrix[0])):
                result.append(matrix[0][i])
            matrix = matrix[1:]
            matrix = self.rotate(matrix)
        return result
            


    def rotate(self, matrix):
        if not matrix: return
        tmp = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0])-1,-1,-1)]
        return tmp
