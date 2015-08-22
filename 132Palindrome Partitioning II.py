##Palindrome Partitioning II
##Given a string s, partition s such that every substring of the partition is a palindrome.
##Return the minimum cuts needed for a palindrome partitioning of s.
##
##2015年8月17日 11:16:09   AC
##zss

class Solution:
    # @param {string} s
    # @return {integer}
    def minCut(self, s):
        dp=[[0 for i in range(len(s))] for j in range(len(s))]
        count=[9999]*(len(s)+1)
        count[len(s)]=0
        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                if s[i]==s[j] and (j-i<2 or dp[i+1][j-1]==1):
                    dp[i][j]=1
                    count[i]=min(count[i],1+count[j+1])
        return count[0]-1
                
            
