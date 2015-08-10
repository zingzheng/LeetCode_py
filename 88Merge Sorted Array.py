##Merge Sorted Array
##Given two sorted integer arrays nums1 and nums2
##merge nums2 into nums1 as one sorted array.
##
##2015年8月4 AC
##zss

class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        while m<len(nums1):
            nums1.pop(-1)
        i = j = 0
        while i<m and j<n:
            if nums2[j]<=nums1[i]:
                nums1.insert(i,nums2[j])
                i += 1
                j += 1
                m += 1
            else:
                i += 1
        nums1.extend(nums2[j:n])
