##3Sum
##Given an array S of n integers, are there elements a, b, c in S
##such that a + b + c = 0?
##Find all unique triplets in the array which gives the sum of zero.

##2015年6月26日   TLE
##zss
##use the solution of 216 Combination Sum

import datetime

##class Solution:
##    # @param {integer[]} nums
##    # @return {integer[][]}
##    def threeSum(self, nums):
##        #print(datetime.datetime.now())
##        if len(nums)<3:
##            return []
##        self.result = []
##        nums.sort()
##        self.choseEle(nums,0,[],3,0)
##        #print(datetime.datetime.now())
##        return self.result
##
##    #candidates is the list that had remove the num chosed
##    #ele is the list that record the num chosed
##    #keep the begini because there is no need to search from begin
##    def choseEle(self, candidates0, target, ele0, deep,begini):
##        ele = ele0[:]
##        candidates = candidates0[:]
##        if deep <= 0:
##            return
##
##        if deep == 1:
##        ##the third num by binary search
##            f = self.findEle(candidates,0,len(candidates)-1,(target-sum(ele)))
##            if f != -1:
##                ele.append(candidates[f])
##                ele.sort()
##                if ele not in self.result:
##                    self.result.append(ele)
##        else:
##        ##the first num by back-tack
##            for i in range(begini,len(candidates)):
##                ele.append(candidates[i])
##                candidates.remove(candidates[i])
##                self.choseEle(candidates, target, ele ,deep-1,i)
##                candidates.insert(i,ele.pop())
##
##    #binary search
##    def findEle(self,candidates,i,j,n):
##        if n<candidates[i] or n>candidates[j] or i>j:
##            return -1
##        mid = (i+j)//2
##        if n == candidates[mid]:
##            return mid
##        elif n < candidates[mid]:
##            return self.findEle(candidates,i,mid-1,n)
##        else:
##            return self.findEle(candidates,mid+1,j,n)
##        




##
##2015年6月27日   AC
##zss


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        #print(datetime.datetime.now())
        result = []
        if len(nums)<3:
            return result
        nums.append(1)
        nums.sort()
        dis = self.binarySearch(nums,0,len(nums)-1,1)
        nums.remove(1)
        for firstn in range(dis):
            for secondn in range(firstn+1,len(nums)-1):
                thirdn = self.binarySearch(nums,secondn+1,len(nums)-1,0-(nums[firstn]+nums[secondn]))
                if thirdn != -1:
                    if[nums[firstn],nums[secondn],nums[thirdn]] not in result:
                        result.append([nums[firstn],nums[secondn],nums[thirdn]])
        #print(datetime.datetime.now())
        return result


    #binary search
    def binarySearch(self,nums,i,j,n):
        if n<nums[i] or n>nums[j] or i>j:
            return -1
        mid = (i+j)//2
        if n == nums[mid]:
            return mid
        elif n < nums[mid]:
            return self.binarySearch(nums,i,mid-1,n)
        else:
            return self.binarySearch(nums,mid+1,j,n)
