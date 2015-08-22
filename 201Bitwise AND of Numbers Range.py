##Bitwise AND of Numbers Range
##Given a range [m, n] where 0 <= m <= n <= 2147483647,
##return the bitwise AND of all numbers in this range, inclusive.
##For example, given the range [5, 7], you should return 4.
##
##2015年8月19日 15:29:50 AC
##zss
##do not completely understand

class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
        offset=0
        while m and n:
            if m==n:return m<<offset
            m>>=1
            n>>=1
            offset+=1
        return 0
