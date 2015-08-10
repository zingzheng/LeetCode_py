##Subsets II
##Given a collection of integers that
##might contain duplicates, nums, return all possible subsets.
##
##2015年8月10日 AC
##zss

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        self.result = []
        self.dic = {}
        nums.sort()
        self.reduce(nums,[])
        return self.result

    def reduce(self,nums0,ele0):
        nums = nums0[:]
        ele = ele0[:]
        if not self.dic.get(str(ele)):
            self.dic[str(ele)] = 1
            self.result.append(ele)
        for i,n in enumerate(nums):
            ele.append(nums.pop(i))
            self.reduce(nums[i:],ele)
            nums.insert(i,n)
            ele.pop(-1)
