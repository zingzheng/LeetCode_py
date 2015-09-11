##Scramble String
##Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
##
##2015年9月10日 14:49:13
##zss
##

##递归  AC
##剪枝：长度不一致，含有字符不一样（统计判断）
##isScramble(s1[:i],s2[:i]) and isScramble(s1[i:],s2[i:])
##or isScramble(s1[:i],s2[i:]) and isScramble(s1[i:],s2[:i])

##class Solution(object):
##    def isScramble(self, s1, s2):
##        """
##        :type s1: str
##        :type s2: str
##        :rtype: bool
##        """
##        length = len(s1)
##        if length!=len(s2):return False
##        if s1==s2:return True
##        count = [0]*26
##        for c in s1:
##            count[ord(c)-97]+=1
##        for c in s2:
##            count[ord(c)-97]-=1
##        for c in count:
##            if c!=0:return False
##        for i in range(1,length):
##            if (self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:])) or (self.isScramble(s1[:i],s2[length-i:]) and self.isScramble(s1[i:],s2[:length-i])):
##                return True
##        return False
            

##动态规划
##dp[length][i][j] = isScramble(s1[i:i+length],s2[j:j+length]

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        length = len(s1)
        if length!=len(s2):return False
        dp = [[[False]*length]*length]*length
        for i in range(length):
            for j in range(length):
                dp[0][i][j]= s1[i]==s2[j]

        for lth in range(2,length+1):
            for i in range(length-lth,-1,-1):
                for j in range(length-lth,-1,-1):
                    for t in range(1,lth):
                        if ((dp[t-1][i][j] and dp[lth-t-1][i+t][j+t])or(dp[t-1][i][j+lth-t] and dp[lth-t-1][i+t][j])):
                            dp[lth-1][i][j]=True
                            break
        return dp[length-1][0][0]                        
        
