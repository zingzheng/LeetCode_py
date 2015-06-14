##Kth Largest Element in an Array
##2015年6月14日 AC
##zss

import heapq

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]
