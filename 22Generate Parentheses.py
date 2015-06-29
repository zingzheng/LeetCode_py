##Generate Parentheses
##Given n pairs of parentheses,
##write a function to generate all combinations of well-formed parentheses.
##For example, given n = 3, a solution set is:
##"((()))", "(()())", "(())()", "()(())", "()()()"
##
##2015年6月29日   AC
##zss

class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        self.result = []
        left = right = n
        self.generate('',left,right)
        return self.result
        

    def generate(self,seq,left,right):
        if left == right == 0:
            self.result.append(seq)
        elif left == right: 
            self.generate(''.join([seq,'(']),left-1,right)
        elif left < right:
            if left:
                self.generate(''.join([seq,'(']),left-1,right)
            if right:
                self.generate(''.join([seq,')']),left,right-1)
            
        
