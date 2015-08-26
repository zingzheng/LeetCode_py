##Binary Tree Paths
##Given a binary tree, return all root-to-leaf paths.
##
##2015年8月23日 19:24:12 AC
##zss

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.result=[]
        self.dfs(root,[])
        return self.result

    def dfs(self,root,path0):
        path = path0[::]
        if not root :return
        path.append(str(root.val))
        if not root.left and not root.right:
            self.result.append('->'.join(path))
        else:
            if root.left:
                self.dfs(root.left,path)
            if root.right:
                self.dfs(root.right,path)
    
