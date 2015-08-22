##Reverse Bits
##Reverse bits of a given 32 bits unsigned integer.
##
##2015年8月19日 11:39:09  AC
##zss

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        int(bin(43261596)[:1:-1].ljust(32,'0'),2)
