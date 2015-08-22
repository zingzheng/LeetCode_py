##Best Time to Buy and Sell Stock
##Say you have an array for which the ith element is the price
##of a given stock on day i.
##If you were only permitted to complete at most one transaction
##(ie, buy one and sell one share of the stock),
##design an algorithm to find the maximum profit.
##
##2015年8月17日 09:24:19 AC
##zss

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if len(prices)<2:return 0
        profit = [0]
        maxProfit = 0
        for i in range(1,len(prices)):
            profit.append(max(profit[-1]+prices[i]-prices[i-1],prices[i]-prices[i-1]))
            maxProfit=max(maxProfit,profit[-1])
        return maxProfit
