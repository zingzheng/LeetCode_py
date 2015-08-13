##Symmetric Tree
##Given a binary tree, check whether it is a mirror of itself
##(ie, symmetric around its center).
##
##2015年8月13日  AC
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
    def isSymmetric(self, root):
        if not root:return True
        return self.isSame(root.left,root.right)

    def isSame(self, p, q):
        if not p and not q: return True
        elif (p and not q) or (q and not p) or p.val != q.val: return False
        else: return self.isSame(p.left,q.right) and self.isSame(p.right,q.left)

    
