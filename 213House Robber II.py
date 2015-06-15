##213House Robber II
##After robbing those houses on that street, the thief has found himself
##a new place for his thievery so that he will not get too much attention.
##This time, all houses at this place are arranged in a circle.
##That means the first house is the neighbor of the last one.
##Meanwhile, the security system for these houses remain the same
##as for those in the previous street.
##
##Given a list of non-negative integers representing the amount of money of
##each house, determine the maximum amount of money you can rob tonight
##without alerting the police
##
##2015年6月14日  AC
##zss

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums)<4:
            return max(nums)
        mm = 0
        #rob1,notrob2,从第3算起（最后一个不能抢劫）
        isrob = pre_isrob = nums[0]+nums[2]
        notrob = pre_notrob = nums[0]
        for i in range(3,len(nums)-1):
            isrob = pre_notrob + nums[i]
            notrob = max(pre_isrob, pre_notrob)
            pre_isrob = isrob
            pre_notrob = notrob
        mm = max(isrob,notrob)
        #notrob1,从第2个算起（最后一个可以选择）
        isrob = pre_isrob = nums[1]
        notrob = pre_notrob = 0
        for i in range(2,len(nums)):
            isrob = pre_notrob + nums[i]
            notrob = max(pre_isrob, pre_notrob)
            pre_isrob = isrob
            pre_notrob = notrob
        return max(isrob,notrob,mm)
            
     
