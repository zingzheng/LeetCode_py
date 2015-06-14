#Validate Binary Search Tree
#Given a binary tree, determine if it is a valid binary search tree (BST).

#2015年6月8日  AC
#zss

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def LDR(self, root):
        if root != None:
            if root.left != None:
                self.LDR(root.left)
            self.tree.append(root.val)
            if root.right != None:
                self.LDR(root.right)
    
    # @param {TreeNode} root
    # @return {boolean}
    def isValidBST(self, root):
        self.tree=[]
        self.LDR(root)
        i=0
        while i<len(self.tree)-1:
            if self.tree[i] >= self.tree[i+1]:
                return False
            i+=1
        return True
