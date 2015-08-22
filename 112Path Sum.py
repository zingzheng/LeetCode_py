##Path Sum
##Given a binary tree and a sum, determine if the tree has a root-to-leaf path
##such that adding up all the values along the path equals the given sum.
##
##2015年8月14日 10:38:23  AC
##zss


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        if not root :return False
        sum -= root.val
        if sum==0 and not root.left and not root.right:return True
        if sum!=0 and not root.left and not root.right:return False
        if root.left and not root.right:return self.hasPathSum(root.left,sum)
        if root.right and not root.left:return self.hasPathSum(root.right,sum)
        if root.right and root.left:return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)
    
