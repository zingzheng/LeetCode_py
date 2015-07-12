##Subsets
##Given a set of distinct integers, nums, return all possible subsets.
##Note:
##Elements in a subset must be in non-descending order.
##The solution set must not contain duplicate subsets.
##
##2015年7月12日  AC
##zss

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        self.result = [[]]
        nums.sort()
        self.reduce(nums,[])
        return self.result

    def reduce(self,nums0,ele0):
        nums = nums0[:]
        ele = ele0[:]
        if ele:
            self.result.append(ele)
        for i,n in enumerate(nums):
            ele.append(nums.pop(i))
            self.reduce(nums[i:],ele)
            nums.insert(i,n)
            ele.pop(-1)
