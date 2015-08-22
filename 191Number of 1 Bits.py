##Number of 1 Bits
##Write a function that takes an unsigned integer and returns the number
##of ’1' bits it has (also known as the Hamming weight).
##For example, the 32-bit integer ’11' has binary representation
##00000000000000000000000000001011, so the function should return 3.
##
##2015年8月19日 14:15:44
##zss

class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        return bin(n).count('1')
