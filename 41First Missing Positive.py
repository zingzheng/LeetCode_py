##First Missing Positive
##Given an unsorted integer array, find the first missing positive integer.
##For example,
##Given [1,2,0] return 3,
##and [3,4,-1,1] return 2.
##Your algorithm should run in O(n) time and uses constant
##
##2015年7月4日  AC
##zss
##put the num in position num-1

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        if not nums:return 1
        index = 0
        while index<len(nums):
            if nums[index]>0 and nums[index]-1!=index and nums[index]-1<len(nums) and nums[index]!=nums[nums[index]-1]:
                indexb = nums[index]-1
                nums[index],nums[indexb] = nums[indexb], nums[index]
            else:
                index += 1
        for i in range(len(nums)):
            if i+1 != nums[i]:
                return i+1
        return len(nums)+1
