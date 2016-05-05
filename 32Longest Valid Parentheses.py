##Longest Valid Parentheses
##Given a string containing just the characters '(' and ')',
##find the length of the longest valid (well-formed) parentheses substring.
##
##2015年7月1日  TLE
##zss

##class Solution:
##    # @param {string} s
##    # @return {integer}
##    def longestValidParentheses(self, s):
##        max_result = 0
##        if not s:return max_result
##        i ,j = 0,1
##        while j<len(s):
##            if s[j] == ')':
##                result,jump = self.testP(s[i:j+1])
##                max_result = max(max_result,result)
##                if jump:
##                    i += jump
##                    j = i
##                elif result== 0 and j == len(s)-1:
##                    #mean exit excess '('
##                    i += 1
##                    j = i
##            j += 1
##        return max_result
##        
##    #return result,i_jump
##    def testP(self,s):
##        result = 0
##        pStack = []
##        for char in s:
##            if char == '(' :
##                pStack.append(char)
##            elif char == ')' and len(pStack) == 0:
##                #if exit excess ')',i shoult jump through
##                return 0,result+1
##            else:
##                result += 2
##                pStack.pop()
##        if pStack:
##            #if exit excess '(',i do not move,j keep moving
##            return 0,0
##        else:
##            #this is a perfet sub,i do not move,j keep moving
##            return result,0


##2015年7月2日
##zss
##动态规划  AC

class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        if not s:return 0
        dp = [0]*len(s)
        for i in range(1,len(s)):
            if s[i] == ')':
                if i-1-dp[i-1]>= 0 and s[i-1-dp[i-1]] == '(':
                    dp[i] = dp[i-1]+2
                    if i-1-dp[i-1]>0:
                        dp[i] = dp[i] + dp[i-1-dp[i-1]-1]
        return max(dp)


