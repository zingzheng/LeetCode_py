##Shortest Palindrome
##Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.
##2015年10月25日 18:27:58
##zss


#TLE
##class Solution(object):
##    def shortestPalindrome(self, s):
##        """
##        :type s: str
##        :rtype: str
##        """
##        s = list(s)[::-1]
##        if s==s[::-1]:
##            return ''.join(s)
##        n = len(s)
##        for i in range(len(s)):
##            s.extend(s[:i][::-1])
##            if s == s[::-1]:
##                return ''.join(s)
##            else:
##                s = s[:n]

##思路：用改进的manacher算以第一个字符开始的最长回文串，把剩下的部分逆序补到头部
##AC
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        pos = self.manacher(s)
        return ''.join([s[pos::][::-1],s])


    def manacher(self,s):
        s1 = list('#'.join(s))
        s1.insert(0,'*')
        s1.append('$')
        p=[0]*len(s1)
        mi,res=0,0 #mi能覆盖右侧最远的回文串中心，res以第一个字符为开始的最大回文串
        for i in range(1,len(s1)-1):
            if i < mi+p[mi]:
                p[i] = min(p[2*mi-i],mi+p[mi]-i)
            else:
                p[i] = 1
            while s1[i+p[i]]==s1[i-p[i]]:
                p[i]+=1
            if mi+p[mi] < i+p[i]:
                mi = i
            if p[i]==i:
                res = max(res,i)
        return res
            
