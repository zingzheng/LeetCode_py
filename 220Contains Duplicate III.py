##Contains Duplicate III 
##Given an array of integers, find out whether there are two distinct
##indices i and j in the array such that
##the difference between nums[i] and nums[j] is at most t
##and the difference between i and j is at most k. 

#2015年6月9日   AC
#zss

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k == 0:
            return False
        numlist = [nums[0]]
        for i in range(1,len(nums)):
            if t == 0:
                if nums[i] in numlist:
                    return True
            else:
                maxn = max(numlist)
                minn = min(numlist)
                if nums[i]-t<=minn or nums[i]+t>=maxn:
                    return True
            
            if len(numlist)>=k:
                numlist.pop(0)
            numlist.append(nums[i])
        return False
        
