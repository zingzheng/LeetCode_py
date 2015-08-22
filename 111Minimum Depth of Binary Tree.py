##Minimum Depth of Binary Tree
##Given a binary tree, find its minimum depth.
##
##2015年8月14日 10:23:56  AC
##zss

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
        if not root:return 0
        if not root.left and root.right:return 1+self.minDepth(root.right)
        if not root.right and root.left:return 1+self.minDepth(root.left)
        return 1+min(self.minDepth(root.left),self.minDepth(root.right))
