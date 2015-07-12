##Valid Number
##Validate if a given string is numeric.
##
##2015年7月8日   AC
##zss

class Solution:
    # @param {string} s
    # @return {boolean}
    def isNumber(self, s):
        inputType = [[' '],['+','-'],
                     ['0','1','2','3','4','5','6','7','8','9'],
                     ['.'],['e','E']]
        transitionTable=[[0,1,2,3,-1,-1],
                         [-1,-1,2,3,-1,-1],
                         [9,-1,2,4,6,-1],
                         [-1,-1,5,-1,-1,-1],
                         [9,-1,5,-1,6,-1],
                         [9,-1,5,-1,6,-1],
                         [-1,7,8,-1,-1,-1],
                         [-1,-1,8,-1,-1,-1],
                         [9,-1,8,-1,-1,-1],
                         [9,-1,-1,-1,-1,-1]]
        state = 0
        for c in s:
            if state == -1:
                return False
            f = 0
            for i in range(5):
                if c in inputType[i]:
                    state = transitionTable[state][i]
                    f = 1
                    break
            if f == 0:
                state = -1
        if state  in(2,4,5,8,9):
            return True
        else:
            return False
