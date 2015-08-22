##Single Number
##Given an array of integers, every element appears twice except for one.
##Find that single one.
##
##2015年8月17日 17:26:13  AC
##zss

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        nset=set()
        for n in nums:
            if n not in nset:
                nset.add(n)
            else:
                nset.remove(n)
        return nset.pop()
                
