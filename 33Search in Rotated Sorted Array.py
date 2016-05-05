##Search in Rotated Sorted Array
##Suppose a sorted array is rotated at some pivot unknown to you beforehand.
##(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
##You are given a target value to search.
##If found in the array return its index, otherwise return -1.
##You may assume no duplicate exists in the array.
##
##2015年7月2日  AC
##zss

class Solution2:
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
            if target == nums[0]: return 0
            elif nums[0]<target<nums[flag]:
                return self.binarySearch(nums,0+1,flag-1,target)
            elif target == nums[flag]:return flag
            else:
                return self.binarySearch(nums,flag+1,len(nums)-1,target)


    #binary search
    def binarySearch(self,nums,i,j,n):
        if n<nums[i] or n>nums[j] or i>j:
            return -1
        mid = (i+j)//2
        if n == nums[mid]:
            return mid
        elif n < nums[mid]:
            return self.binarySearch(nums,i,mid-1,n)
        else:
            return self.binarySearch(nums,mid+1,j,n)


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        low,high = 0,len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:return mid
            #在旋转点的左侧
            if nums[mid]>nums[low]:
                if nums[low]<=target<=nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            #在旋转点右侧
            elif nums[mid]<nums[low]:
                if nums[mid]<=target<=nums[high]:
                    low = mid+1
                else:
                    high = mid-1
            else:low+=1
        return -1
                
