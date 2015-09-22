##Candy
##There are N children standing in a line. Each child is assigned a rating value.
##You are giving candies to these children subjected to the following requirements:
##Each child must have at least one candy.
##Children with a higher rating get more candies than their neighbors.
##What is the minimum candies you must give? 
##
##2015年9月21日 13:54:40  AC
##zss

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        can=[1]*len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i-1]<ratings[i]:
                can[i]=can[i-1]+1
        print(can)
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i+1]<ratings[i] and can[i]<=can[i+1]:
                can[i]=can[i+1]+1
        print(can)
        return sum(can)
            
