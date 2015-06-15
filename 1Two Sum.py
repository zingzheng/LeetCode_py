##1Two Sum
##Given an array of integers, find two numbers such that they add up to
##a specific target number.
##The function twoSum should return indices of the two numbers
##such that they add up to the target, where index1 must be less than index2.
##Please note that your returned answers (both index1 and index2)
##are not zero-based.
##You may assume that each input would have exactly one solution.
##
##2015年6月15  AC
##zss

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        self.rawnums = nums[:]
        nums.sort()
        for  i in range(len(nums)):
            numa,numb  = nums[i],target-nums[i]
            nums.remove(numa)
            if self.getNumb(nums,numb,0,len(nums)):
                a = self.rawnums.index(numa)
                self.rawnums.remove(numa)
                b = self.rawnums.index(numb)
                if a <= b:
                    return[a+1,b+2]
                else:
                    return[b+1,a+1]
            nums.insert(i,numa)
        return []

    def getNumb(self,nums,numb,head,tail):
        
        if head >= tail:
            return False
        if numb>nums[tail-1] or numb<nums[head]:
            return False
        mid = (head+tail)//2
        if nums[mid] == numb:
            return True
        elif nums[mid] > numb:
            return self.getNumb(nums,numb,head,mid)
        elif nums[mid] < numb:
            return self.getNumb(nums,numb,mid+1,tail)
        
        


            


    
