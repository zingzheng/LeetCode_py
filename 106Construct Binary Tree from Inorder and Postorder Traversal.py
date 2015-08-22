##Construct Binary Tree from Inorder and Postorder Traversal
##Given inorder and postorder traversal of a tree, construct the binary tree.
##
##2015年8月13日 21:30:26  AC
##zss

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {integer[]} inorder
    # @param {integer[]} postorder
    # @return {TreeNode}
    def buildTree(self, inorder, postorder):
        if not inorder:return None
        n = postorder[-1]
        i = inorder.index(n)
        postorder.remove(n)
        root = TreeNode(n)
        root.right = self.buildTree(inorder[i+1:],postorder)
        root.left = self.buildTree(inorder[:i],postorder)
        return root
