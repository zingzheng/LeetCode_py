##Maximum Product Subarray
##Find the contiguous subarray within an array (containing at least one number)
##which has the largest product.
##
##2015年8月18日 11:11:04   AC
##zss

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        if not nums:return 0
        if len(nums)==1:return nums[0]
        result=maxP=minP=nums[0]
        for n in nums[1:]:
            minP,maxP = min(n,minP*n,maxP*n),max(n,minP*n,maxP*n)
            result = max(result,maxP)
        return result

                    
                
                
