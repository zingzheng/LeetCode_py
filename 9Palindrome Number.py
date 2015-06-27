##Palindrome Number
##Determine whether an integer is a palindrome. Do this without extra space.
##2015年6月25日  AC
##zss

##class Solution:
##    # @param {integer} x
##    # @return {boolean}
##    def isPalindrome(self, x):
##        if not x or x<0:
##            return False
##        length = len(x)  #no such len
##        h = 0
##        tail = lenth-1
##        while h < tail:
##            print(x//2**(lenth-h-1) %10)
##            print(x//2**(lenth-tail-1) %10)
##            if x//2**(lenth-h-1) %10 != x//2**(lenth-tail-1) %10:
##                return False
##            h += 1
##            tail -= 1
##        return True


class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x == None or x<0:
            return False
        x = str(x)
        h = 0
        t = len(x)-1
        while h < t:
            if x[h] != x[t]:
                return False
            h += 1
            t -= 1
        return True
