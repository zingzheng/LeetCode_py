##Sort Colors
##Given an array with n objects colored red, white or blue,
##sort them so that objects of the same color are adjacent,
##with the colors in the order red, white and blue.
##Here, we will use the integers 0, 1, and 2 to represent the color red, white,
##and blue respectively.
##Note:
##You are not suppose to use the library's sort function for this problem.
##
##2015年7月12日
##zss

##one-pass algorithm using only constant space
class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        if not nums or len(nums)<2:return
        i,j,k = -1,-1,0
        while k<len(nums):
            if nums[k] == 0:
                i+=1
                j+=1
                if i!=j:
                    nums[k],nums[i],nums[j] = nums[j],nums[k],nums[i]
                else:
                    nums[k],nums[i] = nums[i],nums[k]
            elif nums[k] == 1:
                j+=1
                nums[j],nums[k] = nums[k],nums[j]
            k+=1
