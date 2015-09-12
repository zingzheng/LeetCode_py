##Recover Binary Search Tree
##Two elements of a binary search tree (BST) are swapped by mistake.
##Recover the tree without changing its structure.
##
##2015年9月11日 15:06:15  AC
##zss

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.mis1,self.mis2,self.pre=None,None,None
        self.traval(root)
        if self.mis1 and self.mis2:
            self.mis1.val,self.mis2.val=self.mis2.val,self.mis1.val

    def traval(self,root):
        if not root:return
        if root.left:self.traval(root.left)
        if self.pre and root.val<self.pre.val:
            if not self.mis1:
                self.mis1=self.pre
            self.mis2=root
        self.pre = root
        if root.right:self.traval(root.right)
            
        
        
