##Missing Number
##Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
##find the one that is missing from the array.
##
##2015年8月26日 16:23:44  AC
##zss

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        s = sum(nums)
        ss = l*(l+1)//2
        return ss-s
