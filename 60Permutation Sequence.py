##Permutation Sequence
##The set [1,2,3,…,n] contains a total of n! unique permutations.
##Given n and k, return the kth permutation sequence.
##
##2015年7月6日  TLE
##zss

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        result = [i for i in range(1,n+1)]
        for i in range(1,k):
            self.nextPermutation(result)
        return ''.join(str(n) for n in result)

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
            
