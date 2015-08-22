##Valid Palindrome
##Given a string, determine if it is a palindrome,
##considering only alphanumeric characters and ignoring cases.
##
##2015年8月17日 09:30:10     AC
##zss
##

class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        slist = []
        for c in s:
            if c.isalpha() or c.isdigit():
                slist.append(c.lower())
        return slist==slist[::-1]
