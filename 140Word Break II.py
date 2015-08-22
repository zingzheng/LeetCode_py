##Word Break II
##Given a string s and a dictionary of words dict,add spaces in s
##to construct a sentence where each word is a valid dictionary word.
##Return all such possible sentences.
##
##2015年8月17日 19:36:54  AC
##zss

class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    def wordBreak(self, s, wordDict):
        self.dp=[False]*(len(s)+1)
        self.dp[0] = True
        self.result=[]
        self.breaker(s,wordDict)
        self.dfs(s,wordDict,[])
        return self.result

    def dfs(self,s,wordDict,ele0):
        ele = ele0[::]
        if not s:
            self.result.append(' '.join(ele[::-1]))
        else:
            for i in range(len(s)-1,-1,-1):
                if s[i:] in wordDict and self.dp[i]:
                    ele.append(s[i:])
                    self.dfs(s[:i],wordDict,ele)
                    ele.pop(-1)
    



    ##用上一题结论进行减枝
    def breaker(self, s, wordDict):  
        for i in range(1,len(s)+1):
            for j in range(i-1,-1,-1):
                if self.dp[j] and s[j:i] in wordDict:
                    self.dp[i]=True
                    break
