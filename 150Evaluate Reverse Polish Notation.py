##Evaluate Reverse Polish Notation
##Evaluate the value of an arithmetic expression in Reverse Polish Notation.
##Valid operators are +, -, *, /. Each operand may be an integer
##or another expression. 
##
##2015年8月18日 10:16:23  AC
##zss

##-3//5=-1 in python but =0 in C

class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        stack=[]
        for n in tokens:
            if n not in ('+','-','*','/'):
                stack.append(int(n))
            else:
                n2 = stack.pop(-1)
                n1 = stack.pop(-1)
                if n=='+':stack.append(n1+n2)
                elif n=='-':stack.append(n1-n2)
                elif n=='*':stack.append(n1*n2)
                elif n=='/':
                    if n1*n2<0:stack.append(-n1//n2)
                    else:stack.append(n1//n2)
        return stack[0]
