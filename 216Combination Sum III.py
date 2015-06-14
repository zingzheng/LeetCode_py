##Combination Sum
##Find all possible combinations of k numbers that add up to a number n,
##given that only numbers from 1 to 9 can be used
##and each combination should be a unique set of numbers.
##Ensure that numbers within the set are sorted in ascending order.


##2015年6月10日  AC
##zss

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}

    
    def combinationSum3(self, k, n):
        self.result = []
        maxn = (9+10-k)*k/2
        if n<maxn:
            self.choseEle(list(range(1,10)),n,[],k)
        elif n == maxn:
            self.result.append(list(range(10-k,10)))
        return self.result

    def choseEle(self, candidates0, target, ele0, deep):
        ele = ele0[:]
        candidates = candidates0[:]
        if deep <= 0:
            return
        
        for i in range(len(candidates)):
            s = sum(ele)+candidates[i]
            if s == target and deep == 1:
                ele.append(candidates[i])
                ele.sort()
                if ele not in self.result:
                    self.result.append(ele)
                
            elif s < target:
                ele.append(candidates[i])
                candidates.remove(candidates[i])
                self.choseEle(candidates, target, ele ,deep-1)
                candidates.insert(i,ele.pop())
            else:
                break
