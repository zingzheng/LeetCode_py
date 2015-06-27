##Longest Palindromic Substring
##
##2015年6月18日 AC
##zss

class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        if not s or len(s) == 1:
            return s
        subStr = ''
        it = 1
        s = ''.join(['~',s])
        while it < len(s)-1:
            if not(s[it] == s[it+1] or s[it-1] == s[it+1]):
                it += 1
                continue
            
            if s[it] == s[it+1]:
                l = it
                r = it+1
                while l>0 and r<len(s) and s[l]==s[r]:
                    l -= 1
                    r += 1

                if r-l-1 > len(subStr):
                    subStr = s[l+1:r]

            if s[it-1] == s[it+1]:
                l = it-1
                r = it+1
                while l>0 and r<len(s) and s[l]==s[r]:
                    l -= 1
                    r += 1

                if r-l-1 > len(subStr):
                    subStr = s[l+1:r]
                
            it += 1
        return subStr
