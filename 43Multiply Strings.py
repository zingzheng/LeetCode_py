##Multiply Strings
##Given two numbers represented as strings,
##return multiplication of the numbers as a string.
##Note: The numbers can be arbitrarily large and are non-negative.
##
##2015年7月4日  AC
##zss

##class Solution:
##    # @param {string} num1
##    # @param {string} num2
##    # @return {string}
##    def multiply(self, num1, num2):
##        return str(min(2**31-1,int(num1)*int(num2)))

class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        return str(int(num1)*int(num2))
