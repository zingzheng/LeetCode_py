##Pascal's Triangle II
##Given an index k, return the kth row of the Pascal's triangle.
##
##2015年8月14日 14:25:50  AC
##zss

class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        pre=[]
        result=[]
        for row in range(rowIndex+1):
            result = [1]
            for i in range(1,row):
                result.append(pre[i-1]+pre[i])
            if row!=0:result.append(1)
            pre = result[::]
        return result
