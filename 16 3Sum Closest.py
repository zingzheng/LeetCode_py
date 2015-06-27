##3Sum Closest
##Given an array S of n integers, find three integers in S such that
##the sum is closest to a given number, target.
##Return the sum of the three integers.
##You may assume that each input would have exactly one solution.

##2015年6月27日 AC
##zss

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        sumClosest = 999999
        nums.sort()
        for firstn in range(len(nums)-2):
            for secondn in range(firstn+1,len(nums)-1):
                thirdn = self.binarySearch(nums[secondn+1::],0,len(nums[secondn+1::])-1,target-(nums[firstn]+nums[secondn]))
                stmp = nums[firstn]+nums[secondn]+nums[secondn+1::][thirdn]
                if  stmp == target:
                    return target
                else:
                    if abs(stmp-target)<abs(sumClosest-target):
                        sumClosest = stmp
        return sumClosest




    #binary search
    #if no such num return the nearlyst
    def binarySearch(self,nums,i,j,n):
        if n<nums[i]:
            if i == 0:
                return i
            else:
                if abs(nums[i]-n)<abs(nums[i-1]-n):
                    return i
                else:
                    return i-1
        if n>nums[j]:
            if j==len(nums)-1:
                return j
            else:
                if abs(nums[j]-n)<abs(nums[j+1]-n):
                    return j
                else:
                    return j+1
        if i>j:
            if abs(nums[i]-n)<abs(nums[j]-n):
                return i
            else:
                return j
        mid = (i+j)//2
        if n == nums[mid]:
            return mid
        elif n < nums[mid]:
            return self.binarySearch(nums,i,mid-1,n)
        else:
            return self.binarySearch(nums,mid+1,j,n)

