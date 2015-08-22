##Find Minimum in Rotated Sorted Array
##Suppose a sorted array is rotated at some pivot unknown to you beforehand.
##(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
##Find the minimum element.
##You may assume no duplicate exists in the array.
##
##2015年8月18日 14:42:23 AC
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
