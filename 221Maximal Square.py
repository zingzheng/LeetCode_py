##Maximal Square
##Given a 2D binary matrix filled with 0's and 1's,
##find the largest square containing all 1's and return its area.
##
##2015年6月9日 AC
##but need to seek alg cost less time
##zss

class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        
        if not matrix:
            return 0
        maxsize = 0
        isize = len(matrix)
        jsize = len(matrix[0])
        size = min(isize,jsize)
        
        for i in range(isize):
            for j in range(jsize):
                ssize = min(isize-i,jsize-j)
                if maxsize < ssize and matrix[i][j] == '1':
                    #探索最大k
                    tmpsize = 1
                    for k in range(1,ssize):
                        flag = 1
                        for x in range(k+1):
                            if matrix[i+x][j+k] == '0':
                                flag = 0
                                break
                        if not flag:
                            tmpsize = k
                            break
                        for y in range(k+1):
                            if matrix[i+k][j+y] == '0':
                                flag = 0
                                break
                        if not flag:
                            tmpsize = k
                            break
                        tmpsize = k+1
                    if maxsize < tmpsize:
                        maxsize = tmpsize
        return maxsize**2
                            
                            
                                
