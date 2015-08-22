##Single Number II
##Given an array of integers, every element appears three times except for one.
##Find that single one.
##
##2015年8月17日 17:37:21  AC
##zss

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        dic=dict()
        for n in nums:
            if n not in dic:
                dic[n]=1
            elif dic[n]==2:
                dic.pop(n)
            else:
                dic[n]+=1
        return dic.keys()[0]
