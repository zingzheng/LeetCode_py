##Majority Element
##Given an array of size n, find the majority element.
##The majority element is the element that appears more than ⌊ n/2 ⌋ times.
##You may assume that the array is non-empty
##and the majority element always exist in the array.
##
##2015年8月18日 16:54:05  AC
##zss

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        count=0
        for n in nums:
            if count==0:
                result=n
                count+=1
            else:
                if n==result:count+=1
                else:count-=1
        return result
            
