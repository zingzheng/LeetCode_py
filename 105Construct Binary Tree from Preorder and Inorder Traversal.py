##Construct Binary Tree from Preorder and Inorder Traversal
##Given preorder and inorder traversal of a tree, construct the binary tree.
##You may assume that duplicates do not exist in the tree.
##
##2015年8月13日 17:51:06
##zss

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} preorder
    # @param {integer[]} inorder
    # @return {TreeNode}
    def buildTree(self, preorder, inorder):
