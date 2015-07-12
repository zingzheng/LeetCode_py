##Minimum Window Substring
##Given a string S and a string T, find the minimum window in S
##which will contain all the characters in T in complexity O(n).

##2015年7月12日  AC
## zss

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    def minWindow(self, s, t):
        result = ''
        if not t:return result
        dicT = {}
        for char in t:
            if not dicT.get(char):
                dicT[char] = 0
            dicT[char] += 1 
        i=j=0
        while i<len(s) and  s[i] not in t:
                    i += 1
        s = s[i:]
        i = 0
        while j <len(s) or max(dicT.values())<=0:
            if max(dicT.values())<=0:
                ##get window
                if not result:
                    result = s[i:j]
                elif j-i < len(result):
                    result = s[i:j]
                dicT[s[i]] += 1
                i += 1
                while i<len(s) and  s[i] not in t:
                    i += 1
                continue
            while j< len(s) and s[j] not in t:
                j += 1
            if j<len(s):
                dicT[s[j]] -= 1
                j += 1
        return result
