##Divide Two Integers
##Divide two integers without using multiplication, division and mod operator.
##If it is overflow, return MAX_INT.
##
##2015年6月30日 AC
##zss

class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        f = (dividend >0 and divisor>0) or (dividend <0 and divisor<0)
        a,b,result = abs(dividend),abs(divisor),0
        while a>=b:
            it,count = b,0
            while a> (it<<1):
                it<<=1
                count+=1
            a-=it
            result += (1<<count)
        if not f:
            result = -result
        return min(max(-2147483648,result),2147483647)
