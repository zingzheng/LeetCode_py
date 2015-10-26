##Best Time to Buy and Sell Stock IV
##Say you have an array for which the ith element is the price of a given stock on day i.
##Design an algorithm to find the maximum profit. You may complete at most k transactions.
##Note:
##You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
##
##2015年10月25日 16:24:40  AC
##zss

##这道题是比较难的dp题目，很难给出dp的定义，以下定义参考网上的解法
##global[i][j]:=到第i天，最多进行j次交易的最好利润
##local[i][j]:=到第i天，最多进行j次交易，且最后一次交易在第i天卖出的最好利润
##递推公式：
##global[i][j]=max(local[i][j],global[i-1][j])
##local[i][j]=max(global[i-1][j-1]+max(diff,0),local[i-1][j]+diff)

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if k<=0 or n==0:return 0
        result=count=0
        for i in range(1,n):
            if prices[i]-prices[i-1]>0:
                result += prices[i]-prices[i-1]
                count += 1
        if count<=k: ##as same as not limit
            return result
        localProfit =[[0 for j in range(k+1)] for i in range(n)] 
        globalProfit = [[0 for j in range(k+1)] for i in range(n)]
        for j in range(1,k+1):
            for i in range(1,n):
                localProfit[i][j]= max(  
                    localProfit[i - 1][j] + prices[i] - prices[i -1],   
                    globalProfit[i - 1][j - 1] + max(0, prices[i] - prices[i - 1]));  
                globalProfit[i][j] = max(localProfit[i][j], globalProfit[i - 1][j]);
        return globalProfit[-1][-1]
                


        
