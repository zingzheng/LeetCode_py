##House Robber
##You are a professional robber planning to rob houses along a street.
##Each house has a certain amount of money stashed,
##the only constraint stopping you from robbing each of them is that
##adjacent houses have security system connected
##and it will automatically contact the police
##if two adjacent houses were broken into on the same night.
##
##Given a list of non-negative integers representing the amount of money of each house,
##determine the maximum amount of money you can rob tonight without alerting the police.
##
##2015年6月14日  AC
##zss
##抢劫i房子能得到的最多钱为：不抢劫i-1得到的最多钱+该房子的钱
##不抢劫i房子得到的最多钱为：不抢劫i-1得到的最多钱和抢劫i-1房子得到最多钱 两者的最大
##因此只需要记录i-1房子 抢劫和不抢劫分别得到的最多钱即可

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        pre_isrob = pre_notrob = 0
        isrob = notrob =0
        for n in nums:
            isrob = pre_notrob + n
            notrob = max(pre_notrob,pre_isrob)
            pre_notrob = notrob
            pre_isrob = isrob
        return max(notrob,isrob)
            
