##Minimum Size Subarray Sum
##Given an array of n positive integers and a positive integer s,
##find the minimal length of a subarray of which the sum ≥ s.
##If there isn't one, return 0 instead.
##
##2015年8月19日 16:45:33  AC
##zss
##滑动窗口

class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        if not nums:return 0
        minL= 2**31
        total=i=j=0
        while i<=j and j<len(nums) and total<s:
            total+=nums[j]
            while i<=j and total>=s:
                minL = min(minL,j-i+1)
                total-=nums[i]
                i+=1
            j+=1
        return 0 if minL==2**31 else minL
                
                
