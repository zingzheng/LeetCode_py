##Permutations
##Given a collection of numbers, return all possible permutations.
##For example,
##[1,2,3] have the following permutations:
##[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1]. 

##2015年7月5日 AC
##zss

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        self.result = []
        self.generate(nums,[])
        return self.result

    def generate(self,nums0,ele0):
        nums = nums0[::]
        ele = ele0[::]
        if not nums:
            self.result.append(ele)
        else:
            for i,n in enumerate(nums):
                ele.append(n)
                nums.remove(n)
                self.generate(nums,ele)
                nums.insert(i,n)
                ele.remove(n)
        
            
