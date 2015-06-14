##Combination Sum
##Given a set of candidate numbers (C) and a target number (T),
##find all unique combinations in C where the candidate numbers sums to T.
##Each number in C may only be used once in the combination. 

##2015年6月10日  AC
##zss

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}

    
    def combinationSum2(self, candidates, target):
        self.result = []
        candidates.sort()
        self.choseEle(candidates,target,[])
        return self.result

    def choseEle(self, candidates0, target, ele0):
        ele = ele0[:]
        candidates = candidates0[:]
        
        for i in range(len(candidates)):
            s = sum(ele)+candidates[i]
            if s == target:
                ele.append(candidates[i])
                ele.sort()
                if ele not in self.result:
                    self.result.append(ele)
                
            elif s < target:
                ele.append(candidates[i])
                candidates.remove(candidates[i])
                self.choseEle(candidates, target, ele)
                candidates.insert(i,ele.pop())
            else:
                break
