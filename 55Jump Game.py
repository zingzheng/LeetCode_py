##Jump Game
##Given an array of non-negative integers,
##you are initially positioned at the first index of the array.
##Each element in the array represents your maximum jump length at that position.
##Determine if you are able to reach the last index. 

##2015年7月4日 AC
##zss

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        if not nums:return False
        maxstep = 0
        for i,n in enumerate(nums):
            if i>maxstep:return False
            maxstep = max(maxstep,i+n)
        return True
