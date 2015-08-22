##Find Minimum in Rotated Sorted Array II
##Find the minimum element.
##The array may contain duplicates.
##
##2015年8月18日 14:50:29  AC
##zss

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        if not nums:return
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                return nums[i+1]
        return nums[0]
