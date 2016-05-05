##Regular Expression Matching
##Implement regular expression matching with support for '.' and '*'.
##2015年6月25日   AC
##zss
import re
class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        pattern = re.compile(p)
        match = pattern.match(s)
        if match:
            if match.group() == s:
                return True
        return False
            
        



class Solution:
        # @param {string} s
        # @param {string} p
        # @return {boolean}
        def isMatch(self, s, p):
            lens,lenp = len(s),len(p)
            dp = [[False]*(lenp+1) for i in range(lens+1)]
            dp[0][0]=True
            for j in range(2,lenp+1):
                dp[0][j] = dp[0][j-2] and p[j-1]=='*'
                
            for i in range(1,lens+1):
                for j in range(1,lenp+1):
                    if p[j-1]=='*':
                        dp[i][j] = dp[i][j-2] or dp[i-1][j] and p[j-2] in (s[i-1],'.')
                    else:
                        dp[i][j]=dp[i-1][j-1] and p[j-1] in (s[i-1],'.')
            return dp[lens][lenp]
