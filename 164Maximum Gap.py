##Maximum Gap
##Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
##Try to solve it in linear time/space.
##Return 0 if the array contains less than 2 elements.
##You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
##
##2015年9月22日 18:08:11  AC
##zss
##桶排序
##鸽巢原理  假设有N个元素A到B。那么最大差值不会小于[(B - A) / (N - 1)]
##令桶的大小为[(B - A) / (N - 1)]，最大差值出现在相邻效同之间

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length<2:
            return 0
        max_int,min_int=2**31-1,-(2**31)
        maxN,minN = max(nums),min(nums)
        if maxN==minN:return 0
        bucket = 1.0*(maxN-minN)/(length-1)
        minI = [max_int]*length
        maxI = [min_int]*length
        for n in nums:
            bucketId = int((n-minN)/bucket)
            print(n,bucketId)
            minI[bucketId] = min(minI[bucketId],n)
            maxI[bucketId] = max(maxI[bucketId],n)
        print(minI,maxI)
        result=0
        preMax=maxI[0]
        for i in range(1,length):
            if minI[i]!=max_int:
                result = max(result,minI[i]-preMax)
                preMax = maxI[i]
        return result
        
        
