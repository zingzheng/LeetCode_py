##Remove Element
##Given an array and a value, remove all instances of that value
##in place and return the new length.
##The order of elements can be changed.
##It doesn't matter what you leave beyond the new length.
##
##2015年6月30日  AC
##zss
##

class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        if not nums: return 0
        lenth,i,j= len(nums),0,len(nums)-1
        while i <= j:
            if nums[i] == val:
                nums[i],nums[j] = nums[j],nums[i]
                j -= 1
                lenth -=1
            else:
                i += 1
        return lenth
