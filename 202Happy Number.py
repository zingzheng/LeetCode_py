##Happy Number
##Write an algorithm to determine if a number is "happy".
##A happy number is a number defined by the following process:
##Starting with any positive integer,
##replace the number by the sum of the squares of its digits,
##and repeat the process until the number equals 1 (where it will stay),
##or it loops endlessly in a cycle which does not include 1.
##Those numbers for which this process ends in 1 are happy numbers.

##2015年6月11日 AC
##zss

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        num = n
        numset = {n}
        if n<=0:
            return False
        while True:
            strnum = str(num)
            num = 0
            for i in range(len(strnum)):
                num += int(strnum[i])**2
            if num == 1:
                return True
            elif num in numset:
                return False
            else:
                numset.add(num)
