##Palindrome Partitioning
##Given a string s, partition s such that every substring of the partition is a palindrome.
##Return all possible palindrome partitioning of s.
##
##2015年8月17日 11:02:17  AC
##zss

class Solution:
    # @param {string} s
    # @return {string[][]}
    def partition(self, s):
        self.result=[]
        self.dfs(s,[])
        return self.result
        
    def dfs(self,s,dp0):
        dp = dp0[::]
        if not s:
            if dp:self.result.append(dp)
        else:
            for i in range(len(s)):
                tmp = s[:i+1]
                if tmp == tmp[::-1]:
                    dp.append(tmp)
                    self.dfs(s[i+1:],dp)
                    dp.pop(-1)
