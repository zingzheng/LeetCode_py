##Integer to Roman
##Given an integer, convert it to a roman numeral.
##Input is guaranteed to be within the range from 1 to 3999.
##
##2015年6月25日  AC
##zss

class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        roman=''
        roman = ''.join([roman,'M'*(num//1000)])
        num %= 1000
        if num//100<4:
            roman = ''.join([roman,'C'*(num//100)])
        elif num//100==4:
            roman = ''.join([roman,'CD'])
        elif num//100<9:
            roman = ''.join([roman,'D','C'*(num//100-5)])
        else:
            roman = ''.join([roman,'CM'])                
        num %= 100
        if num//10<4:
            roman = ''.join([roman,'X'*(num//10)])
        elif num//10==4:
            roman = ''.join([roman,'XL'])
        elif num//10<9:
            roman = ''.join([roman,'L','X'*(num//10-5)])
        else:
            roman = ''.join([roman,'XC']) 
        num %= 10
        if num<4:
            roman = ''.join([roman,'I'*num])
        elif num==4:
            roman = ''.join([roman,'IV'])
        elif num<9:
            roman = ''.join([roman,'V','I'*(num-5)])
        else:
            roman = ''.join([roman,'IX'])
        return roman
