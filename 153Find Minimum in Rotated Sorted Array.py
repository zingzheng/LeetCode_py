##Find Minimum in Rotated Sorted Array
##Suppose a sorted array is rotated at some pivot unknown to you beforehand.
##(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
##Find the minimum element.
##You may assume no duplicate exists in the array.
##
##2015年8月18日 14:42:23 AC
##zss

class Solution2:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        if not nums:return
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                return nums[i+1]
        return nums[0]

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        low,hight=0,len(nums)-1
        while low<=hight:
            ##最后指向同一个元素，或指向一个正序区间
            if nums[low]<=nums[hight]:
                return nums[low]
            else:
                mid=(low+hight)//2
                ##旋转点在mid右侧
                if nums[mid]>=nums[low]:
                    low=mid+1
                ##旋转点恰好是mid或在mid左侧
                else:
                    if nums[mid]<nums[mid-1]:
                        return nums[mid]
                    hight=mid-1
