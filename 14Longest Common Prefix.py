##Longest Common Prefix
##Write a function to find the longest common prefix string
##amongst an array of
##2015年6月26日  AC
##zss

class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        if len(strs)==1:
            return strs[0]
        for i in range(1,len(strs[0])+1):
            for j in range(1,len(strs)):
                if strs[j].find(strs[0][:i:])!=0:
                    if not i:
                        return ''
                    else:
                        return strs[0][:i-1:]
        return strs[0]
