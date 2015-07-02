##Search Insert Position
##Given a sorted array and a target value,
##return the index if the target is found.
##If not, return the index where it would be if it were inserted in order.
##You may assume no duplicates in the array.
##
##2015年7月2日  AC
##zss

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        return self.binarySearch(nums,0,len(nums)-1,target)


    #binary search
    def binarySearch(self,nums,i,j,n):
        if i > j:
            return i
        if n<nums[i]:
            return i
        if n>nums[j]:
            return j+1
        mid = (i+j)//2
        if n == nums[mid]:
            return mid
        elif n < nums[mid]:
            return self.binarySearch(nums,i,mid-1,n)
        else:
            return self.binarySearch(nums,mid+1,j,n)
