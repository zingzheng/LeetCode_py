##Valid Parentheses
##Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
##determine if the input string is valid.
##The brackets must close in the correct order,
##"()" and "()[]{}" are all valid but "(]" and "([)]" are not.
##
##2015年6月29日  AC
##zss

class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        m = {'(':')','[':']','{':'}'}
        stacklist = []
        for p in s:
            if p in('(','{','['):
                stacklist.append(p)
            else:
                if not stacklist or p != m[stacklist[-1]]:
                    return False
                else:
                    stacklist.pop()

        if not stacklist:
            return True
        else:
            return False
