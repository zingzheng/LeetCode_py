##Plus One
##Given a non-negative number represented as an array of digits,
##plus one to the number.
##The digits are stored such that the most significant digit is
##at the head of the list.
##
##2015年7月9日  AC
##zss

class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        if not digits:
            return digits
        c = 0
        digits[-1] += 1
        for i in range(len(digits)-1,-1,-1):
            digits[i] += c
            if digits[i] == 10:
                digits[i] = 0
                c = 1
            else:
                c = 0
                break
        if c == 1:
             d = [1]
             d.extend(digits)
             digits = d
        return digits
