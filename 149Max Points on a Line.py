##Max Points on a Line
##Given n points on a 2D plane, find the maximum number of points that
##lie on the same straight line.
##
##2015年9月22日 15:05:33  AC
##zss

# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points)<3:
            return len(points)
        mx=0
        for p1 in points:
            dic={}
            same=0
            for p2 in points:
                if p1.x==p2.x and p1.y==p2.y:
                    same+=1
                    continue
                elif p1.x==p2.x:
                    k='None'
                else:
                    k=1.0*(p1.y-p2.y)/(p1.x-p2.x)
                if k not in dic:
                    dic[k]=0
                dic[k]+=1
            if dic:
                mx=max(mx,max(dic.values())+same)
            else:
                mx=max(mx,same)
        return mx
        
