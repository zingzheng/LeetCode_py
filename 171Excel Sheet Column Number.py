##Excel Sheet Column Number
##Given a column title as appear in an Excel sheet, return its corresponding column number.
##
##2015年8月18日 17:04:52  ac
##zss

class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        result =0
        for c in s:
            result=result*26+ord(c)-64
        return result

