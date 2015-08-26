##Lowest Common Ancestor of a Binary Tree
##Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
##
##2015年8月21日 18:16:05  AC
##zss
##bottom-up

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        if root==p or root==q:return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left and right:return root
        return left if left else right
