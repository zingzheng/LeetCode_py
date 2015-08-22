##Reverse Words in a String
##Given an input string, reverse the string word by word.
##
##2015年8月18日 10:56:18  AC
##zss

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return ' '.join(s.split()[::-1])
