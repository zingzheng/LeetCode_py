##Next Permutation
##
##2015年7月1日 AC
##zss
##从后往前找到第一对相邻且升序，记左边的数字位置begin
##从后往前找到第一个比nums[begin]大的数字，记位置为end
##交换begin和end，并把begin后的数字位置逆序

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
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
        
        
        
