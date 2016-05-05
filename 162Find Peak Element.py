##Find Peak Element
##A peak element is an element that is greater than its neighbors.
##Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
##The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
##You may imagine that num[-1] = num[n] = -∞.
##For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
##
##2015年9月22日 17:25:04  AC
##zss

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:return None
        if len(nums)==1:return 0
        if nums[1]<nums[0]:return 0
        if nums[-2]<nums[-1]:return len(nums)-1
        for i in range(1,len(nums)-1):
            if nums[i-1]<nums[i]>nums[i+1]:
                return i


class Solution(object):
    def findPeakElement(self, nums):
        low,high = 0,len(nums)-1
        while low <= high:
            if low==high:
                return low
            mid = (low+high)//2
            if num[mid]<num[mid+1]:
                low+=1
            else:
                high=mid
