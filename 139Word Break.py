##Word Break
##Given a string s and a dictionary of words dict,
##determine if s can be segmented into a space-separated sequence of one
##or more dictionary words.
##
##2015年8月17日  AC
##zss

##dp  长度为i的字符串能被分割=长度为j的字符串能被分割，且s[j:i]在字典中

class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(1,len(s)+1):
            for j in range(i-1,-1,-1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i]=True
                    break
        return dp[len(s)]
                    
