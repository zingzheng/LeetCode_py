##Gray Code
##
##The gray code is a binary numeral system where two successive values
##differ in only one bit.
##Given a non-negative integer n representing the total number of bits
##in the code, print the sequence of gray code. A gray code sequence must
##begin with 0.
##For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
##
##00 - 0
##01 - 1
##11 - 3
##10 - 2
##
##2015年8月10日 AC
##zss

class Solution:
    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
        if not n: return [0]
        a = ['0','1']
        while n>1:
            i = len(a)-1
            for str in a[::-1]:
                a[i] = ''.join(['0',str])
                a.append(''.join(['1',str]))
                i -= 1
            n -= 1
        return [int(str,2) for str in a]
