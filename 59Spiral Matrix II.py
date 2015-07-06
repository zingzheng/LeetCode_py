##Spiral Matrix II
##Given an integer n,
##generate a square matrix filled with elements from 1 to n2 in spiral order.
##
##2015年7月6日   AC
##zss

class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        result= [[0 for i in range(n)] for j in range(n)]
        matrix= [[(i,j) for j in range(n)] for i in range(n)]
        count = 1
        while matrix:   
            for i in range(len(matrix[0])):
                result[matrix[0][i][0]][matrix[0][i][1]]=count
                count += 1
            matrix = matrix[1:]
            matrix =self.rotate(matrix)
        return result

    def rotate(self, matrix):
        if not matrix: return
        tmp = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0])-1,-1,-1)]
        return tmp
