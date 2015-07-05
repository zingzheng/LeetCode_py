##Trapping Rain Water
##2015年7月4日   AC
##zss

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        i=result=0
        while i<len(height):
            if height[i] == 0:
                i += 1
            else:
                print(i,height[i])
                right,index = self.findRight(height,i)
                print(index,right)
                if right:
                    space = (index-i-1)*min(right,height[i])-sum(height[i+1:index])
                    result += space
                    i = index
                else:
                    return result
        return result

    def findRight(self,nums,i):
        if len(nums)-i <=1:
            return 0,0
        ##return the first whilch bigger than nums[i]
        for index in range(i+1,len(nums)):
            if nums[index]>nums[i]:
                return nums[index],index
        ##no num bigger than nums[i],return the biggest
        max_right = max(nums[i+1::])
        return max_right,nums[i+1::].index(max_right)+i+1
            
        
                                                       
