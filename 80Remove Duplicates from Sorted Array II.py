##Remove Duplicates from Sorted Array II
##Follow up for "Remove Duplicates":
##What if duplicates are allowed at most twice?
##For example,
##Given sorted array nums = [1,1,1,2,2,3],
##Your function should return length = 5, w
##ith the first five elements of nums being 1, 1, 2, 2 and 3.
##It doesn't matter what you leave beyond the new length.
##
##2015年7月13日  AC
##zss


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        dic = {}
        length=i= 0
        while i <len(nums):
            n = nums[i]
            if not dic.get(n):
                dic[n] = 0
            dic[n] += 1
            if dic.get(n)>2:
                nums.remove(n)
            else:
                i += 1
                length += 1
        return length
