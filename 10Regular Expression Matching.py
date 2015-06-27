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
            
        
