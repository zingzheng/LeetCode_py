##Wildcard Matching
##
##2015年7月4日
##zss

##  TLE
## "abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb", "**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb"

##import re
##
##class Solution:
##    # @param {string} s
##    # @param {string} p
##    # @return {boolean}
##    def isMatch(self, s, p):
##        ##kill mul *
##        plist = [p[i] for i in range(len(p))]
##        i=1
##        while i<len(plist):
##            if plist[i]==plist[i-1]=='*':
##                plist.pop(i)
##            else:
##                i+=1
##        p = ''.join(plist)        
##        p = p.replace('*','.*')
##        p = p.replace('?','.')
##        print(p)
##        return self.regularMatch(s,p)
##
##    def regularMatch(self, s, p):
##        pattern = re.compile(p)
##        match = pattern.match(s)
##        if match:
##            if match.group() == s:
##                return True
##        return False

##AC
import re
class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        if p == s:
            return True
        if not p:
            return False
        p = p.replace('?','.')
        ##split p by '*'
        plist = p.split('*')
        begin = 0
        for i,psplit in enumerate(plist):
            if '.' in psplit:
                ##last one
                if i == len(plist)-1:
                    begin = self.regularMatch(s,psplit,begin,1)
                    if p[-1]!='*' and begin+len(psplit) !=len(s):
                        return False
                else:
                    begin = self.regularMatch(s,psplit,begin,0)
                if begin == -1:
                    return False
                ## first one
                if i==0 and p[0] != '*' and begin!= 0:
                    return False
                begin += len(psplit)
            else:
                ##last one
                if i == len(plist)-1:
                    lb = s.rfind(psplit)
                    if lb < begin:
                        return False
                    else:
                        begin = lb
                        if p[-1]!='*' and begin+len(psplit) !=len(s):
                            return False
                else:
                    begin = s.find(psplit,begin)
                if begin == -1:
                    return False
                ##first one
                if i==0 and p[0] != '*' and begin!= 0:
                    return False
                begin += len(psplit)
        return True
            
    def regularMatch(self, s, p,begin,islast):
            pattern = re.compile(p)
            result = pattern.search(s,begin)
            if not result:
                return -1
            if not islast:
                return result.start()
            if islast:
                while result:
                    begin = result.start()
                    result = pattern.search(s,begin+1)
                return begin
        
        
        
