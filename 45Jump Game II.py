##Jump Game II
##Given an array of non-negative integers,
##you are initially positioned at the first index of the array.
##Each element in the array represents your maximum jump length at that position.
##Your goal is to reach the last index in the minimum number of jumps.
##For example:
##Given array A = [2,3,1,1,4]
##The minimum number of jumps to reach the last index is 2.
##(Jump 1 step from index 0 to 1, then 3 steps to the last index.) 

##2015年7月5日  AC
##zss

##each next step is the max through  over

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        step = maxPos = nextPos =0
        for i,n in enumerate(nums):
            if i>nextPos:
                step += 1
                nextPos = maxPos
            maxPos = max(maxPos,i+n)
        return step
