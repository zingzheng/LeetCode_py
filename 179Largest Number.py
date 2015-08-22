##Largest Number
##Given a list of non negative integers,
##arrange them such that they form the largest number.
##For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
##Note: The result may be very large, so you need to return a string instead of an integer.
##
##2015年8月19日 09:07:12
##zss
## cmp only fit in python 2.x

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        return str(int(''.join(sorted(map(str, nums), cmp=lambda a, b: cmp(b+a, a+b)))))
                
