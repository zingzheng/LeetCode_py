##Reverse Integer
##2015年6月24日  AC
##zss

class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        if not x: return x
        f = 1
        if x<0: f = -1
        strx = str(x*f)
        intx = int(strx[::-1])
        return f*intx*(intx<2**31)
