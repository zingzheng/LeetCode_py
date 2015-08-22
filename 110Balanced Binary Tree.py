##Balanced Binary Tree
##Given a binary tree, determine if it is height-balanced.
##For this problem, a height-balanced binary tree is defined as a binary tree
##in which the depth of the two subtrees of every node never differ by more than 1.
##
##2015年8月14日 09:09:43  AC
##zss

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        if not root:return True
        return abs(self.maxDepth(root.left)-self.maxDepth(root.right))<2 and self.isBalanced(root.left) and self.isBalanced(root.right)
    def maxDepth(self, root):
        if not root:return 0
        else:return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

