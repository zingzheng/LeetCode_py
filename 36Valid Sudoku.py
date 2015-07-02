##Valid Sudoku
##Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
##The Sudoku board could be partially filled, where empty cells are filled
##with the character '.'
##
##2015年7月2日  AC
##zss


class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        row = board
        column = [[board[i][j] for i in range(9)]for j in range(9)]
        b = [board[i][j]  for count1 in range(0,9,3) for count2 in range(0,9,3) for i in range(0+count1,3+count1) for j in range(0+count2,3+count2)]
        box  = [[b[i+count] for i in range(0,9)]for count in range(0,80,9)]
        for i in row:
            for j in i:
                if j!='.' and i.count(j)>1:
                    return False
        for i in column:
            for j in i:
                if j!='.' and i.count(j)>1:
                    return False
        for i in box:
            for j in i:
                if j!='.' and i.count(j)>1:
                    return False
        return True
