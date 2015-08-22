##Best Time to Buy and Sell Stock II
##Say you have an array for which the ith element is the price
##of a given stock on day i.
##Design an algorithm to find the maximum profit.
##You may complete as many transactions as you like
##(ie, buy one and sell one share of the stock multiple times).
##However, you may not engage in multiple transactions at the same time
##(ie, you must sell the stock before you buy again).
##
##2015年8月17日 09:26:02 AC
##zss

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        profit=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profit+=prices[i]-prices[i-1]
            else:
                continue
        return profit
