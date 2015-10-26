##Dungeon Game
##
##2015年9月23日 09:41:08  AC
##zss

##从右下角进行动态规划，计算在每个点时，骑士至少需要多少点魔法

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m,n = len(dungeon),len(dungeon[0])
        dp = [[0 for i in range(n)]for j in range(m)]
        dp[-1][-1]=0 if dungeon[-1][-1]>=0 else -dungeon[-1][-1]
        for i in range(m-2,-1,-1):
            dp[i][-1]=0 if dungeon[i][-1]>=dp[i+1][-1] else dp[i+1][-1]-dungeon[i][-1]
        for j in range(n-2,-1,-1):
            dp[-1][j]=0 if dungeon[-1][j]>=dp[-1][j+1] else dp[-1][j+1]-dungeon[-1][j]
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                down = 0 if dungeon[i][j]>=dp[i+1][j] else dp[i+1][j]-dungeon[i][j]
                right = 0 if dungeon[i][j]>=dp[i][j+1] else dp[i][j+1]-dungeon[i][j]
                dp[i][j]=min(down,right)
        return dp[0][0]+1
