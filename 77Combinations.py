##Combinations
##Given two integers n and k, return all possible combinations of
##k numbers out of 1 ... n.
## 
##2015年7月12日   AC
##zss

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        self.result = []
        nums = list(range(1,n+1))
        self.reduce(nums,[],k)
        return self.result

    def reduce(self,nums0,ele0,k):
        nums = nums0[:]
        ele = ele0[:]
        if k == 0:
            self.result.append(ele)
        else:
            for i,n in enumerate(nums):
                ele.append(nums.pop(i))
                self.reduce(nums[i:],ele,k-1)
                nums.insert(i,n)
                ele.pop(-1)
