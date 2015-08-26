##Single Number III
##Given an array of numbers nums, in which exactly two elements appear only once
##and all the other elements appear exactly twice.
##Find the two elements that appear only once.

##2015年8月26日 15:30:27  AC
##zss

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = set()
        for n in nums:
            if n in s:
                s.remove(n)
            else:
                s.add(n)
        return list(s)
