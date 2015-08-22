##Best Time to Buy and Sell Stock III
##Say you have an array for which the ith element is the price
##of a given stock on day i.
##Design an algorithm to find the maximum profit.
##You may complete at most two transactions.
##
##2015年8月17日 09:28:47 AC
##zss

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if len(prices)<2:return 0
        left=[0]
        right=[0]
        for i in range(1,len(prices)):
            left.append(max(prices[i]-prices[i-1],prices[i]-prices[i-1]+left[-1]))
        maxPrices = prices[-1]
        for i in range(len(prices)-2,-1,-1):
            maxPrices = max(maxPrices,prices[i])
            right.insert(0,max(right[0],maxPrices-prices[i]))
        left = [left[i]+right[i] for i in range(len(prices))]
        return max(left)
