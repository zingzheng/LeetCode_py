##Search in Rotated Sorted Array II
##Follow up for "Search in Rotated Sorted Array":
##What if duplicates are allowed?
##Would this affect the run-time complexity? How and why?
##Write a function to determine if a given target is in the array.
##
##2015年7月13日 AC
##zss
##

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        flag = -1
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                flag = i
                break
        
        if flag == -1:
            return self.binarySearch(nums,0,len(nums)-1,target)
        else:
            if target == nums[0]: return True
            elif nums[0]<target<nums[flag]:
                return self.binarySearch(nums,0+1,flag-1,target)
            elif target == nums[flag]:return True
            else:
                return self.binarySearch(nums,flag+1,len(nums)-1,target)


    #binary search
    def binarySearch(self,nums,i,j,n):
        if n<nums[i] or n>nums[j] or i>j:
            return False
        mid = (i+j)//2
        if n == nums[mid]:
            return True
        elif n < nums[mid]:
            return self.binarySearch(nums,i,mid-1,n)
        else:
            return self.binarySearch(nums,mid+1,j,n)
        
