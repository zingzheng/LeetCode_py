##Compare Version Numbers
##Compare two version numbers version1 and version2.
##If version1 > version2 return 1,
##if version1 < version2 return -1,
##otherwise return 0.
##You may assume that the version strings are non-empty
##and contain only digits and the . character.
##The . character does not represent a decimal point
##and is used to separate number sequences.
##For instance, 2.5 is not "two and a half" or "half way to version three",
##it is the fifth second-level revision of the second first-level revision.
##Here is an example of version numbers ordering:
##0.1 < 1.1 < 1.2 < 13.37
##
##2015年8月18日 15:38:51  AC
##zss

class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        left1,right1=self.splitVersion(version1)
        left2,right2=self.splitVersion(version2)
        if left1>left2:return 1
        elif left1<left2:return -1
        elif left1==left2 and not right1 and not right2:return 0
        else:
            return self.compareVersion(right1,right2)

    def splitVersion(self,version):
        if not version:return 0,''
        i = version.find('.')
        if i==-1:
            return int(version),''
        return int(version[:i]),version[i+1:]
        
