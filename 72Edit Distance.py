##Edit Distance
##Given two words word1 and word2,
##find the minimum number of steps required to convert word1 to word2.
##(each operation is counted as 1 step.)
##You have the following 3 operations permitted on a word:
##a) Insert a character
##b) Delete a character
##c) Replace a character
##
##2015年7月12日  AC
##zss
##DP

class Solution:
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def minDistance(self, word1, word2):
        d = [[0 for j in range(len(word2)+1)]for i in range(len(word1)+1)]
        for i in range(len(word1)+1):
            for j in range(len(word2)+1):
                if i == 0:
                    d[i][j] = j
                elif j == 0:
                    d[i][j] = i
                elif word1[i-1] == word2[j-1]:
                    d[i][j] = d[i-1][j-1]
                else:
                    d[i][j] = min(d[i-1][j-1],d[i][j-1],d[i-1][j])+1
        return d[-1][-1]
