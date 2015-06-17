##Longest Substring Without Repeating Characters
##Given a string, find the length of the longest substring
##withoutrepeating characters.
##For example, the longest substring without repeating letters for "abcabcbb"
##is "abc", which the length is 3.
##For "bbbbb" the longest substring is "b", with the length of 1.
##
##2015年6月17日  AC
##zss

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        s = ''.join([s,'#'])
        i = 0
        j = i+1
        max = 1
        while j < len(s):
            index  = s[i:j].find(s[j])
            if index >= 0 or s[j] == '#':
                if j - i > max:
                    max = j-i
                i += index+1
            j += 1
        return max
