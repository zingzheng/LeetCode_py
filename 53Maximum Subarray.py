##Maximum Subarray
##Find the contiguous subarray within an array (containing at least one number)
##which has the largest sum.

##2015年7月6日 AC
##zss

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        if not nums: return 0
        result = [nums[0]]
        for i in range(1,len(nums)):
            result.append(nums[i] if result[i-1]<=0 else result[i-1]+nums[i])
        return max(result)
