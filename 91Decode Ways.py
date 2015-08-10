##Decode Ways
##A message containing letters from A-Z is being encoded to numbers
##using the following mapping:
##'A' -> 1
##'B' -> 2
##...
##'Z' -> 26
##Given an encoded message containing digits,
##determine the total number of ways to decode it.
##
##2015年8月10日
##zss

class Solution:
    # @param {string} s
    # @return {integer}
    def numDecodings(self, s):
        if not s: return 0
        count = [1]
        if s[-1] == '0':
            count.append(0)
        else:
            count.append(1)
        for i in range(2,len(s)+1):
            c = 0 if s[-i]=='0' else count[-1]
            if '10'<=s[-i:][0:2]<='26':
                print(s[-i:][0:2])
                c += count[-2]
            count.append(c)
        return count[-1]
