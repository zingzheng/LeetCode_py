##Pow(x, n)
##2015年7月6日 AC
##zss
##

class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        return x**n

class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if n==0:return 1
        return x* self.myPow(x,n-1)
