##Binary Tree Maximum Path Sum
##Given a binary tree, find the maximum path sum.
##The path may start and end at any node in the tree.
##
##2015年9月15日 09:34:52  AC
##zss

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:return 0
        self.maxv = -(2**31)
        self.maxSum(root)
        return self.maxv
    
    def maxSum(self,root):
        if not root:return 0
        v,lmax,rmax=root.val,0,0
        if root.left:
            lmax=self.maxSum(root.left)
            if lmax>0:
                v+=lmax
        if root.right:
            rmax=self.maxSum(root.right)
            if rmax>0:
                v+=rmax
        self.maxv=max(self.maxv,v)
        return max(root.val,root.val+lmax,root.val+rmax)
            
        
