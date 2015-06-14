##Contains Duplicate
##Given an array of integers, find if the array contains any duplicates.
##Your function should return true if any value appears at least twice
##in the array, and it should return false if every element is distinct. 

##2015年6月10日
##zss  AC

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        numset = set()
        la = 0
        for i in range(len(nums)):
            numset.add(nums[i])
            lb = len(numset)
            if la == lb:
                return True
            la = lb
        return False
            
