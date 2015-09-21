##Word Ladder
##Given two words (beginWord and endWord), and a dictionary, find the length of shortest transformation sequence from beginWord to endWord, such that:
##Only one letter can be changed at a time
##Each intermediate word must exist in the dictionary
##
##2015年9月15日 11:14:42  
##zss


##TLE
##class Solution(object):
##    def ladderLength(self, beginWord, endWord, wordDict):
##        """
##        :type beginWord: str
##        :type endWord: str
##        :type wordDict: Set[str]
##        :rtype: int
##        """
##        dic={}
##        dic[0]=beginWord
##        dic[1]=endWord
##        c=2
##        for word in wordDict:
##            dic[c]=word
##            c+=1
##        table=[[0 for i in range(c)]for j in range(c)]
##        for i in range(c):
##            for j in range(i+1,c):
##                #print(dic[i],dic[j],self.changeAble(dic[i],dic[j]))
##                if self.changeAble(dic[i],dic[j]):
##                    table[i][j],table[j][i]=1,1
##        bfs,deep=[0],1
##        while bfs:
##            tmp=[]
##            while dfs:
##                word=bfs.pop()
##                print(dic[word])
##                for i in range(c):
##                    if table[word][i]==1:
##                        if deep==1 and dic[i]==endWord:
##                            continue
##                        else:
##                            if dic[i]==endWord:
##                                return deep+1
##                            if dic[i] in wordDict:
##                                tmp.append(i)
##                                wordDict.remove(dic[i])
##            deep+=1
##            bfs.extend(tmp)
##            
##            
##                
##            
##
##
##    ##if worda can change to wordb,return 1 else 0
##    def changeAble(self,a,b):
##        diff=0
##        if len(a)!=len(b) or a==b:return 0
##        for i in range(len(a)):
##            if a[i]!=b[i]:
##                diff+=1
##                if diff>1:
##                    return 0
##        return 1


##AC
##不直接建图，通过替换字母找下一跳
##用字典记录层，某个word的层=上一跳层数+1
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordDict):
        """
        :type beginWord: str
        :type endWord: str
        :type wordDict: Set[str]
        :rtype: int
        """
        letter=[chr(97+i) for i in range(26)]
        queue=[beginWord]
        dic={beginWord:1}
        while queue:
            word = queue.pop(0)
            level = dic[word]
            
            for i in range(len(word)):
                tmpword = list(word)
                for j in letter:
                    if tmpword[i]==j:continue
                    tmpword[i]=j
                    tmp = ''.join(tmpword)
                    if tmp==endWord:return level+1
                    if tmp in wordDict and tmp not in dic:
                        queue.append(tmp)
                        dic[tmp]=level+1

        return 0
