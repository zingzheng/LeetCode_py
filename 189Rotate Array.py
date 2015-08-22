##Rotate Array
##Rotate an array of n elements to the right by k steps.
##For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is
##rotated to [5,6,7,1,2,3,4].
##
##2015年8月19日 11:20:15  AC
##zss

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        for i in range(k):
            nums.insert(0,nums.pop(-1))
