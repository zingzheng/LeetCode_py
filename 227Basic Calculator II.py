##Basic Calculator II
##Implement a basic calculator to evaluate a simple expression string.
##The expression string contains only non-negative integers, +, -, *, / operators
##and empty spaces . The integer division should truncate toward zero.
##You may assume that the given expression is always valid.
##
##2015年8月19日 17:39:22   AC
##zss

class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        s += '#'
        num = 0
        a = b = None
        preop = op = None
        for c in s:
            if c in ('+','-','*','/','#'):
                if op is None:
                    a = num
                elif op in ('+','-'):
                    if preop is None:
                        b = num
                    else:
                        a = a + b if preop == '+' else a - b
                        b = num
                    preop = op
                else:
                    if preop is None:
                        a = a * num if op == '*' else a / num
                    else:
                        b = b * num if op == '*' else b / num
                op = c
                num = 0
            elif c != ' ':
                num = num * 10 + int(c)
        if preop is None:
            return a
        return a + b if preop == '+' else a - b

