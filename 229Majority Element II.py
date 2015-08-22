##Majority Element II
##Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
##The algorithm should run in linear time and in O(1) space.
##
##2015年8月21日 15:12:03 AC
##zss

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]
        a=b=ca=cb=0
        for n in nums:
            if n==a:ca+=1
            elif n==b:cb+=1
            elif ca==0:
                a=n
                ca+=1
            elif cb==0:
                b=n
                cb+=1
            else:
                ca-=1
                cb-=1
        ca=cb=0
        for n in nums:
            if n==a:ca+=1
            elif n==b:cb+=1
        l = len(nums)//3
        if ca > l:result.append(a)
        if cb> l:result.append(b)
        return result
