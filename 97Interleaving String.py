##Interleaving String
##Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
##2015年9月10日 18:52:04   
##zss

##TLE
##class Solution(object):
##    def isInterleave(self, s1, s2, s3):
##        """
##        :type s1: str
##        :type s2: str
##        :type s3: str
##        :rtype: bool
##        """
##        if not (s1 or s2 or s3):return True
##        if len(s1)+len(s2)!=len(s3):return False
##        if not s2:return s1==s3
##        elif not s1:return s2==s3
##        else:
##            if s1[0]!=s3[0] and s2[0]!=s3[0]:return False
##            elif s1[0]==s3[0] and s2[0]==s3[0]:
##                return self.isInterleave(s1[1:],s2,s3[1:]) or self.isInterleave(s1,s2[1:],s3[1:])
##            elif s1[0]==s3[0]:return self.isInterleave(s1[1:],s2,s3[1:])
##            elif s2[0]==s3[0]:return self.isInterleave(s1,s2[1:],s3[1:])
        

##dp  AC
##dp[i+1][j+1]:表示s1[0...i]与s2[0...j]能否交替形成s3[0...i+j+1]部分.
##dp[i+1][j+1] = (dp[i][j+1] && s1[i] == s3[i+j+1]) | (dp[i+1][j] && s2[j] == s3[i+j+1]);

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if not s2:return s1==s3
        elif not s1:return s2==s3
        len1,len2=len(s1),len(s2)
        if len1+len2!=len(s3):return False
        dp = [[False for i in range(len2+1)] for j in range(len1+1)]
        dp[0][0] = True
        for i in range(len2):
            dp[0][i+1] = (dp[0][i] and s2[i]==s3[i])
        for i in range(len1):
            dp[i+1][0] = (dp[i][0] and s1[i]==s3[i])
        for i in range(len1):
            for j in range(len2):
                dp[i+1][j+1] = ((dp[i][j+1] and s1[i]==s3[i+j+1]) or
                                (dp[i+1][j] and s2[j]==s3[i+j+1]))
        return dp[len1][len2]
