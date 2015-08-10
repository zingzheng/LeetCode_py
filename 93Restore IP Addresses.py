##Restore IP Addresses
##Given a string containing only digits,
##restore it by returning all possible valid IP address combinations.
##
##2015年8月10日  AC
##zss
##
class Solution:
    # @param {string} s
    # @return {string[]}
    def restoreIpAddresses(self, s):
        self.result = []
        self.reduce(s,[])
        return self.result
    def reduce(self,s0,ele0):
        s = s0[::]
        ele = ele0[::]
        if len(ele)==4 and not s:
            self.result.append('.'.join(ele))
        elif len(ele)<4 and s:
            for i in range(1,len(s)+1):
                if int(s[:i])<256:
                    if len(s[:i])>1 and s[0]=='0':
                        break
                    ele.append(s[:i])
                    self.reduce(s[i:],ele)
                    ele.pop(-1)
                else:
                    break
        
