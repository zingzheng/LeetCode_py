##Implement strStr()
##Returns the index of the first occurrence of needle in haystack,
##or -1 if needle is not part of haystack.
##
##2015年6月30日  AC
##zss

class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        return haystack.find(needle)
