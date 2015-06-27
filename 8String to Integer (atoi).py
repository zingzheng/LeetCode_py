##String to Integer (atoi)
##2015年6月24日  AC
##zss

class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        str = str.lstrip()
        if not str: return 0
        for i in range(len(str)):
            if not('0'<=str[i]<='9' or str[i] in('+','-')):
                str = str[:i:]
                break
        try:
            f = 1
            intx = int(str)
            if intx >= 2147483647:
                intx = 2147483647
            elif intx <= -2147483648:
                intx = -2147483648
            return intx
        except:
            return 0
