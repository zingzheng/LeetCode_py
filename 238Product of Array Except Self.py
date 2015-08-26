##Product of Array Except Self
##Given an array of n integers where n > 1, nums,return an array output such that
##output[i] is equal to the product of all the elements of nums except nums[i].
##Solve it without division and in O(n).

##2015年8月22日 10:41:08  AC
##zss

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:return nums
        up=[1]
        down=[1]
        for i in range(1,len(nums)):
            up.append(up[-1]*nums[i-1])
        for i in range(len(nums)-2,-1,-1):
            down.append(down[-1]*nums[i+1])
        down=down[::-1]
        up = [up[i]*down[i] for i in range(len(up))]
        return up
