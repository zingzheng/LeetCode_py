##Pascal's Triangle
##Given numRows, generate the first numRows of Pascal's triangle
##
##2015年8月14日 14:13:07  AC
##zss

class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        result = []
        for row in range(numRows):
            tmp = [1]
            for i in range(1,row):
                tmp.append(result[-1][i-1]+result[-1][i])
            if row!=0:tmp.append(1)
            result.append(tmp)
        return result
