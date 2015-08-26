##Ugly Number II
##Write a program to find the n-th ugly number.
##Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
##For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
##Note that 1 is typically treated as an ugly number. 
##
##2015年8月26日 15:53:30  AC
##zss


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=0:return False
        if n==1:return 1
        uglyList=[1]
        t2=t3=t5=0
        for i in range(1,n):
            uglyList.append(min(uglyList[t2]*2,uglyList[t3]*3,uglyList[t5]*5))
            if uglyList[-1] == uglyList[t2]*2:t2+=1
            if uglyList[-1] == uglyList[t3]*3:t3+=1
            if uglyList[-1] == uglyList[t5]*5:t5+=1
        return uglyList[-1]
