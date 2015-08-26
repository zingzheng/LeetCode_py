##Valid Anagram
##Given two strings s and t,write a function to determine if t is an anagram of s.
##
##2015年8月23日 19:17:58  AC
##zss

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic={}
        for c in s:
            if c not in dic:
                dic[c]=0
            dic[c]+=1
        for c in t:
            if c not in dic or dic[c]==0:
                return False
            dic[c]-=1
        for n in dic.values():
            if n >0:return False
        return True
