##Container With Most Water
##Given n non-negative integers a1, a2, ..., an,
##where each represents a point at coordinate (i, ai).
##n vertical lines are drawn such that the two endpoints of line i
##is at (i, ai) and (i, 0).
##Find two lines, which together with x-axis forms a container,
##such that the container contains the most water.
##Note: You may not slant the container. 

##2015年6月25   AC
##zss

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        h,t = 0,len(height)-1
        result = 0
        while h<t:
            result = max(result,min(height[h],height[t])*(t-h))
            if height[h]<height[t]:
                h+=1
            else:
                t-=1
        return result
