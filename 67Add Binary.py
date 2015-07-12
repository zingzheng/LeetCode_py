##Add Binary
##Given two binary strings, return their sum (also a binary string). 

##2015年7月9日   AC
##zss

class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        return bin(int(a,2)+int(b,2)).split('b')[1]
        
