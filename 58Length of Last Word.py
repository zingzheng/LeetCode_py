#Length of Last Word
#Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
#return the length of last word in the string.
#If the last word does not exist, return 0.

#2015年6月8日 AC
#zss

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        strlist = s.split()
        if strlist :
            return len(strlist[-1])
        return 0;
