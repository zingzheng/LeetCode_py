##Anagrams
##Given an array of strings, return all groups of strings that are anagrams.
##
##2015年7月6   AC
##zss

class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        strsDir = {}
        result = []
        for i,str in enumerate(strs):
            tmp = "".join((lambda x:(x.sort(),x)[1])(list(str)))
            if not strsDir.get(tmp):
                strsDir[tmp] = []
            strsDir[tmp].append(i)
        for value in strsDir.values():
            if len(value) >1:
                for index in value:
                    result.append(strs[index])
                    
        return result
