##Distinct Subsequences
##Given a string S and a string T, count the number of distinct subsequences of T in S.
##A subsequence of a string is a new string which is formed from the original string
##by deleting some (can be none) of the characters without disturbing the relative
##positions of the remaining characters.
##
##2015年9月12日 14:12:23  AC
##zss

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if not(s and t):return 0
        c1,c2 = len(s),len(t)
        if c1<c2:return 0
        dp=[[0 for i in range(c2+1)] for j in range(c1+1)]
        for i in range(c1+1):dp[i][0] = 1
        for i in range(1,c1+1):
            for j in range(1,c2+1):
                dp[i][j]=dp[i-1][j]
                if s[i-1]==t[j-1]:
                    dp[i][j]+=dp[i-1][j-1]
        return dp[-1][-1]
