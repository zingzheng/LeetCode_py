##207Course Schedule
##There are a total of n courses you have to take, labeled from 0 to n - 1.
##Some courses may have prerequisites,
##for example to take course 0 you have to first take course 1,
##which is expressed as a pair: [0,1]
##Given the total number of courses and a list of prerequisite pairs,
##is it possible for you to finish all courses?
##
##2015年6月14日  AC
##zss

class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        inCount = [0]*numCourses
        listC = list(range(numCourses))
        dicC = {}
        for fromC,toC in prerequisites:
            inCount[toC] += 1
            if fromC not in dicC:
                dicC[fromC] = []
            dicC[fromC].append(toC)

        i = 0
        while i < len(listC):
            edge = listC[i]
            if inCount[edge] == 0:
                listC.remove(edge)
                if dicC.get(edge):
                    for to in dicC.get(edge):
                        inCount[to] -= 1
                i = 0
            else:
                i += 1

        return len(listC) == 0
                        
                        
                    
            
            
