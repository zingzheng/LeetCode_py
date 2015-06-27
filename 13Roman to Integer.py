##Roman to Integer
##Given a roman numeral, convert it to an integer.
##Input is guaranteed to be within the range from 1 to 3999.
##2015年6月25日   ac
##zss

class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        ints = pre = 0
        mp = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in range(len(s)):
            if mp[s[i]]<=pre:
                ints += mp[s[i]]
            else:
                ints = ints - 2*pre + mp[s[i]]
            pre = mp[s[i]]
        return ints
            
