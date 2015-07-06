##Permutations II
##Given a collection of numbers that might contain duplicates,
##return all possible unique permutations.
##
##For example,
##[1,1,2] have the following unique permutations:
##[1,1,2], [1,2,1], and [2,1,1].
##
##2015年7月5日  AC
##zss


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, nums):
        basicNums = nums[::]
        result = [basicNums]
        while True:
            nums = self.nextPermutation(nums)
            if nums != basicNums:
                result.append(nums)
            else:
                break
        return result

    def nextPermutation(self, nums0):
        nums = nums0[::]
        if  nums and len(nums)!=1:
            begin=-1
            for i in range(len(nums)-1,0,-1):
                if nums[i-1]<nums[i]:
                    begin = i-1
                    break
            if begin == -1:
                nums.sort()
            else:
                for i in range(len(nums)-1,begin,-1):
                    if nums[i]>nums[begin]:
                        end = i
                        break
                nums[begin],nums[end] = nums[end],nums[begin]
                begin,end = begin+1,len(nums)-1
                while begin<=end:
                    nums[begin],nums[end] = nums[end],nums[begin]
                    begin+=1
                    end-=1
        return nums
