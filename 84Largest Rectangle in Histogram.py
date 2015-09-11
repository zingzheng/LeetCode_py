##Largest Rectangle in Histogram
##
##2015年7月20日   TLE
##zss

##class Solution:
##    # @param {integer[]} height
##    # @return {integer}
##    def largestRectangleArea(self, height):
##        l = len(height)
##        if l == 0:
##            return 0
##        maxArea = nextStep = 0
##        while nextStep >= 0:
##            i = j = nextStep
##            minH = height[i]
##            while j < l:
##                minH = min(minH,height[j])
##                maxArea = max((j-i+1)*minH,maxArea)
##                print(i,j,(j-i+1)*minH)
##                j += 1
##            get = 0
##            for it in range(i+1,l):
##                if height[it]>=height[it-1]:
##                   get = 1
##                   break
##            nextStep = it if get else -1
##                
##        return maxArea 
                

##class Solution:
##    # @param {integer[]} height
##    # @return {integer}
##    def largestRectangleArea(self, height):
##        i = maxArea = 0
##        stack = []
##        length = len(height)
##        while i < length:
##            print(i,stack)
##            if not stack or height[stack[-1]] < height[i]:
##                stack.append(i)
##                i += 1
##            else:
##                width = i if not stack else i-len(stack)-1
##                maxArea = max(maxArea,height[stack.pop(-1)]*width)
##            
##        while stack:
##            width = length if not stack else length-len(stack)-1
##            maxArea = max(maxArea,height[stack.pop(-1)]*width)
##        return maxArea


##强行制造递增

class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack=[]
        height.append(0)
        i=largest=0
        while i < len(height):
            if len(stack)==0 or  height[i]>height[stack[-1]]:
                stack.append(i)
                i+=1
            else:
                tmp = stack.pop(-1)
                largest = max(largest,height[tmp]*(i if len(stack)==0 else i-stack[-1]-1))
        return largest
        
