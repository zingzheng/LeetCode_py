##Add Digits
##Given a non-negative integer num, repeatedly add all its digits
##until the result has only one digit.
##
##2015年8月23日 19:32:48  
##zss

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if not num:return num
        return (num-1)%9+1
