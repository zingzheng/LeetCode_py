##Excel Sheet Column Title
##Given a positive integer, return its corresponding column title
##as appear in an Excel sheet.
##    1 -> A
##    2 -> B
##    3 -> C
##    ...
##    26 -> Z
##    27 -> AA
##    28 -> AB
##
##2015年8月18日 16:44:24  AC
##zss

class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        result=''
        while n>0:
            result = ''.join([chr(65+(n-1)%26),result])
            n = (n-1)//26
        return result
        
