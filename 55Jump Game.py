##Jump Game
##Given an array of non-negative integers,
##you are initially positioned at the first index of the array.
##Each element in the array represents your maximum jump length at that position.
##Determine if you are able to reach the last index. 

##2015年7月4日  WA
##zss

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        if not nums:return False
        i = 0
        while True:
            if i == len(nums)-1:
                return True
            if i >= len(nums) or nums[i]==0:
                return False
            i += nums[i]
