##Power of Two
##Given an integer, write a function to determine if it is a power of two.
##
##2015年8月21日 16:04:17 AC
##zss

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==2 or n==1:
            return True
        if n<1 or n %2 !=0:
            return False
        return self.isPowerOfTwo(n//2)
