##Rectangle Area
##Find the total area covered by two rectilinear rectangles in a 2D plane.
##Each rectangle is defined by its bottom left corner and top right corner
##
##2015年6月9日 AC
##zss

class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        area = (D-B)*(C-A) + (H-F)*(G-E)
        X1 = max(A,E)
        Y1 = max(B,F)
        X2 = min(C,G)
        Y2 = min(D,H)
        if X1 >= X2 or Y1 >= Y2:
            return area
        else:
            return area - (X2-X1)*(Y2-Y1)
