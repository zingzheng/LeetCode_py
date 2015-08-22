##Summary Ranges
##Given a sorted integer array without duplicates, return the summary of its ranges.
##For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
##
##2015年8月21日 14:39:19  AC
##zss

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result=[]
        if not nums:return result
        begin=None
        for i,n in enumerate(nums):
            if begin==None:
                begin=n
            else:
                if n != nums[i-1]+1:
                    result.append(self.toString(begin,nums[i-1]))
                    begin = n
        result.append(self.toString(begin,nums[-1]))
        return result
                
            

    def toString(self,begin,end):
        if begin==end:
            return str(begin)
        return str(begin)+'->'+str(end)
        
