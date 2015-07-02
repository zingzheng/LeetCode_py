##Search for a Range
##Given a sorted array of integers, find the starting and ending position of a given target value.
##Your algorithm's runtime complexity must be in the order of O(log n).
##If the target is not found in the array, return [-1, -1].
##
##2015年7月2日  AC
##zss

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        if not nums:return [-1,-1]
        begin = end = -1
        flag = self.binarySearch(nums,0,len(nums)-1,target)
        i = flag
        while i !=-1:
            begin = i
            i = self.binarySearch(nums,0,i-1,target)
        i = flag
        while i!=-1:
            end = i
            i = self.binarySearch(nums,i+1,len(nums)-1,target)
        return [begin,end]
                
    
    #binary search
    def binarySearch(self,nums,i,j,n):
        if i>j or n<nums[i] or n>nums[j]:
            return -1
        mid = (i+j)//2
        if n == nums[mid]:
            return mid
        elif n < nums[mid]:
            return self.binarySearch(nums,i,mid-1,n)
        else:
            return self.binarySearch(nums,mid+1,j,n)
