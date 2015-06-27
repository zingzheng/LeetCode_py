##6ZigZag Conversion
##
##2015年6月18日  AC
##zss

class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        zig = [[] for i in range(numRows)]
        if numRows == 2:
            return ''.join([''.join(s[::2]),''.join(s[1::2])])
        for i in range(len(s)):
            rn = i%(2*numRows-2)
            if rn<numRows:
                zig[i%(2*numRows-2)].append(s[i])
            else:
                zig[2*numRows-2-rn].append(s[i])
        return ''.join(''.join(zig[i]) for i in range(numRows))
            
