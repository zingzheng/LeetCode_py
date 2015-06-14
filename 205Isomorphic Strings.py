##Isomorphic Strings
##Given two strings s and t, determine if they are isomorphic.
##Two strings are isomorphic if the characters in s can be replaced to get t.
##All occurrences of a character must be replaced with another character
##while preserving the order of characters.
##No two characters may map to the same character but a character may map to itself.
##
##2015年6月10日  AC
##zss  

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        replaceMap={}
        replaceMap2={}
        news = s
        for i in range(len(s)):
            tmp = replaceMap.get(t[i])
            tmp2 = replaceMap2.get(s[i])
            if tmp:
                if tmp != s[i]:
                    #存在多个字母映射到同一个字母
                    return False
            else:
                replaceMap[t[i]] = s[i]

            if tmp2:
                if tmp2 != t[i]:
                    #存在一个字母映射到多个字母
                    return False
            else:
                replaceMap2[s[i]] = t[i]
        return True
