##Substring with Concatenation of All Words
##You are given a string, s, and a list of words, words,
##that are all of the same length.
##Find all starting indices of substring(s) in s that is a concatenation
##of each word in words exactly once and without any intervening characters.
##
##2015年7月1日  AC
##zss
##

class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        result,wordDir = [],{}
        if not s or not words:
            return result
        for w in words:
            if wordDir.get(w):
                wordDir[w] += 1
            else:
                wordDir[w] =1
        i = j =0
        slen,wordlen,wordslen = len(s),len(words[0]),len(words[0])*len(words)
        while i+wordslen<= slen:
            tag = wordDir.copy()
            j = i
            while j+wordlen <= slen:
                count = tag.get(s[j:j+wordlen])
                if count and count != 1:
                    tag[s[j:j+wordlen]] -= 1
                    j += wordlen
                elif count and count ==1:
                    del tag[s[j:j+wordlen]]
                    j += wordlen
                else:
                    break
            if not tag:
                result.append(i)
            i+=1
        return result
