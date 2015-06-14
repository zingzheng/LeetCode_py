##Combination Sum
##Given a set of candidate numbers (C) and a target number (T),
##find all unique combinations in C where the candidate numbers sums to T.
##The same repeated number may be chosen from C unlimited number of times. 

##2015年6月10日  AC
##zss

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}

    
    def combinationSum(self, candidates, target):
        self.result = []
        candidates.sort()
        self.choseEle(candidates,target,[])
        return self.result

    def choseEle(self, candidates, target, ele0):
        ele = ele0[:]
        for i in range(len(candidates)):
            s = sum(ele)+candidates[i]
            if s == target:
                ele.append(candidates[i])
                ele.sort()
                if ele not in self.result:
                    self.result.append(ele)
                
            elif s < target:
                ele.append(candidates[i])
                self.choseEle(candidates, target, ele)
                ele.pop()
            else:
                break
