##The Skyline Problem
##
##2015年10月26日 18:54:01
##zss

##MemoryError
##class Solution(object):
##    def getSkyline(self, buildings):
##        """
##        :type buildings: List[List[int]]
##        :rtype: List[List[int]]
##        """
##        res = []
##        sky = [0]*(buildings[-1][1]+2)
##        for b in buildings:
##            for i in range(b[0],b[1]+1):
##                sky[i] = max(sky[i],b[2])
##        for i in range(1,len(sky)):
##            if sky[i] > sky[i-1]:
##                res.append([i,sky[i]])
##            elif sky[i] < sky[i-1]:
##                res.append([i-1,sky[i]])
##        return res


##TLE
# Definition for a building.
class bu(object):
    def __init__(self, b=[0,0,0]):
        self.l = b[0]
        self.r = b[1]
        self.h = b[2]
    
            
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        stack = []
        if not buildings:return res
        while buildings:
            print("bu--:",buildings)
            print("st--:",stack)
            b1 = buildings.pop()
            flag = True
            for b2 in stack:
                if b2[0]<b1[1]<=b2[1] or b1[0]<b2[1]<=b1[1]:
                    stack.remove(b2)
                    for j,b in enumerate(self.cut(b1,b2)):
                        buildings.append(b)
                    flag = False
                    break
            if flag:
                stack.append(b1)
                    
        pre = stack[0]
        res.append([pre[0],pre[2]])
        for i in range(1,len(stack)):
            if stack[i][0]!=pre[1]:
                res.append([pre[1],0])
                res.append([stack[i][0],stack[i][2]])
            else:
                if stack[i][2]!=pre[2]:
                    res.append([stack[i][0],stack[i][2]])
            
            pre=stack[i]
        res.append([stack[-1][1],0])
        return res


    def cut(self,a,b):
        print(a,b)
        if a[0]<b[0] or (a[0]==b[0] and a[1]<b[1]):
            b1=bu(a)
            b2=bu(b)
        else:
            b1=bu(b)
            b2=bu(a)
        #cut to two parts
        if b1.l<b2.l<b1.r<b2.r:
            if b1.h>=b2.h:
                return [[b1.l,b1.r,b1.h],[b1.r,b2.r,b2.h]]
            else:
                return [[b1.l,b2.l,b1.h],[b2.l,b2.r,b2.h]]
        #cut to three parts or one
        elif b1.l< b2.l<b2.r <b1.r:
            if b2.h>b1.h:
                return [[b1.l,b2.l,b1.h],[b2.l,b2.r,b2.h],[b2.r,b1.r,b1.h]]
            else:
                return [[b1.l,b1.r,b1.h]]
        elif b1.l == b2.l:
            if b1.r == b2.r:
                return [[b1.l,b1.r,max(b1.h,b2.h)]]
            elif b1.h<=b2.h:
                return [[b2.l,b2.r,b2.h]]
            else:
                return [[b1.l,b1.r,b1.h],[b1.r,b2.r,b2.h]]
        elif b1.r == b2.r:
            if b1.h>=b2.h:
                return [[b1.l,b1.r,b1.h]]
            else:
                return [[b1.l,b2.l,b1.h],[b2.l,b2.r,b2.h]]
            
