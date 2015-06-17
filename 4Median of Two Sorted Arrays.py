##Median of Two Sorted Arrays
##There are two sorted arrays nums1 and nums2 of size m and n respectively.
##Find the median of the two sorted arrays.
##The overall run time complexity should be O(log (m+n)).
##
##2015年6月17日  AC
##zss


class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        if not(len1 or len2):
            return 0.0
        ln = rn = 0
        if (len1+len2)%2 == 0:
            lmid = (len1+len2)/2
            rmid = lmid + 1
        else:
            lmid = rmid = (len1+len2+1)/2

        i = j = 0
        while True:
            if j==len2 or (i < len1 and nums1[i] <= nums2[j]):
                num = nums1[i]
                i += 1
            elif i == len1 or(j < len2 and nums2[j] <= nums1[i]):
                num = nums2[j]
                j += 1
            if  i+j == lmid:
                ln = num
            if i+j == rmid:
                rn = num
                return (ln+rn)/2
