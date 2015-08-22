##Fraction to Recurring Decimal
##Given two integers representing the numerator and denominator of a fraction,
##return the fraction in string format.
##If the fractional part is repeating, enclose the repeating part in parentheses.
##
##2015年8月18日 15:57:54 AC
##zss

class Solution:
    # @param {integer} numerator
    # @param {integer} denominator
    # @return {string}
    def fractionToDecimal(self, numerator, denominator):
        if numerator==0 or denominator==0:return '0'
        m=[]
        result=''
        if numerator*denominator<0:
            result=''.join(['-',result])
        numerator,denominator=abs(numerator),abs(denominator)
        a=numerator//denominator
        b=numerator%denominator
        result=''.join([result,str(a)])
        if not b:return result
        else:
            result=''.join([result,'.'])
            while b and b not in m:
                m.append(b)
                numerator=b*10
                a=numerator//denominator
                b=numerator%denominator
                result=''.join([result,str(a)])
            if not b:return result
            else:
                i=m.index(b)-len(m)
                return ''.join([result[:len(result)+i],'(',result[len(result)+i:],')'])
                
