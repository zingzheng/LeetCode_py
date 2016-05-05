class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low,high=1,len(nums)-1
        while low<=high:
            if low==high:
                return low
            mid=(high+low-1)//2
            count=0
            for n in nums:
                if low<=n<=mid:
                    count+=1
            if count>(high-low+1)//2:
                high=mid
            else:
                low=mid+1
