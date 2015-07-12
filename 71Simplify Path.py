##Simplify Path
##Given an absolute path for a file (Unix-style), simplify it.
##For example,
##path = "/home/", => "/home"
##path = "/a/./b/../../c/", => "/c"
##
##2015年7月10日   AC
##zss

class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        stack = []
        for p in path.split('/'):
            if not p or p == '.':
                continue
            elif p == '..':
                if stack:
                    stack.pop(-1)
            else:
                stack.append(p)
        return '/' + '/'.join(stack)
                
