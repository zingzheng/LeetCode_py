##Longest Consecutive Sequence
##Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
##
##2015年9月21日 10:53:56  AC
##zss

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.s = set(nums)
        res=0
        while self.s:
            n=self.s.pop()
            res = max(self.search(n-1,True)+self.search(n+1,False)+1,res)
        return res

    def search(self,n,asc):
        res=0
        while n in self.s:
            self.s.remove(n)
            res+=1
            if asc:n-=1
            else:n+=1
        return res
