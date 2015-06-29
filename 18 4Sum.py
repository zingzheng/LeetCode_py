##4sum
##Given an array S of n integers, are there elements a, b, c, and d in S
##such that a + b + c + d = target?
##Find all unique quadruplets in the array which gives the sum of target.
##
##2015年6月28日  AC
##zss


class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        result = []
        sumdir = {}
        if len(nums)<4:
            return result
        nums.sort()
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                sumlist = sumdir.get(target - (nums[i]+nums[j]))
                if sumlist:
                    for na,nb in sumlist:
                        if i not in(na,nb) and j not in(na,nb):
                            tmp = [nums[i],nums[j],nums[na],nums[nb]]
                            tmp.sort()
                            if tmp not in result:
                                result.append(tmp)
                if  not sumdir.get(nums[i]+nums[j]):
                    sumdir[nums[i]+nums[j]] = []
                sumdir[nums[i]+nums[j]].append([i,j])
        return result
