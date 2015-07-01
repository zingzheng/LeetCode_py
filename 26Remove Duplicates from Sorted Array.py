##Remove Duplicates from Sorted Array
##Given a sorted array, remove the duplicates in place such that
##each element appear only once and return the new length.
##Do not allocate extra space for another array,
##you must do this in place with constant memory.
##
##2015年6月30日  AC
##zss

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        lenth = i = 1
        while i < len(nums):
            if nums[i-1] != nums[i]:
                lenth += 1
                i += 1
            else:
                nums.remove(nums[i])
        return lenth
