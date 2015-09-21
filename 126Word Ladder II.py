##Word Ladder II
##Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:
##Only one letter can be changed at a time
##Each intermediate word must exist in the word list
##
##2015年9月21日 08:59:27  AC
##zss

##基于上一题，记录前一跳

class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        letter=[chr(97+i) for i in range(26)]
        queue=[beginWord]
        dic={beginWord:1}
        self.father={beginWord:{}}
        self.res=[]
        end=2**31
        while queue:

            word = queue.pop(0)
            level = dic[word]
            if level>end:
                break

            for i in range(len(word)):
                tmpword = list(word)
                for j in letter:
                    if tmpword[i]==j:continue
                    tmpword[i]=j
                    tmp=''.join(tmpword)
                    if tmp==endWord:
                        end=level
                    if (tmp in wordlist and (tmp not in dic or dic[tmp]>=level+1)) or tmp==endWord:
                        if tmp not in self.father:
                            self.father[tmp]=set()
                        self.father[tmp].add(word)
                        if tmp not in dic and tmp!=endWord:
                            queue.append(tmp)
                            dic[tmp]=level+1

        self.buildPath([endWord])
        return self.res

    def buildPath(self,path0):
        path=path0[::]
        if path[-1] not in self.father:return
        if not self.father[path[-1]]:
            self.res.append(path[::-1])
        for p in self.father[path[-1]]:
            path.append(p)
            self.buildPath(path)
            path.pop(-1)
