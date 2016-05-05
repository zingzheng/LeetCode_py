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
        ##return haystack.find(needle)
        lenN,lenH=len(needle),len(haystack)
        if lenN>lenH:
            return -1
        elif not needle or haystack[:lenN]==needle:
            return 0
        else:
            res = self.strStr(haystack[1:],needle)
            return 1+res if res!=-1 else -1
            
            
        
