#15.3Sum solution2
#2016年2月24日 17:28:19

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        dic={}
        result=[]
        for n in nums:
            if n not in dic:dic[n]=1
            else: dic[n]+=1
        for a in nums:
            dic[a]-=1
            for b in nums:
                if dic[b]>0:
                    dic[b]-=1
                    if 0-a-b in dic and dic[0-a-b]>0 and sorted([a,b,0-a-b]) not in result:
                        result.append(sorted([a,b,0-a-b]))
                    dic[b]+=1
            dic[a]+=1
        return result
                
