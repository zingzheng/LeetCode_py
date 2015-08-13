##Unique Binary Search Trees II
##Given n, generate all structurally unique BST's (binary search trees)
##that store values 1...n.
##
##2015年8月12日  AC
##zss

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {integer} n
    # @return {TreeNode[]}
    def generateTrees(self, n):
        return self.creatTrees(1,n)
        
    def creatTrees(self,start,end):
        result = []
        if start>end:
            result.append(None)
            return result
        for i in range(start,end+1):
            lefts = self.creatTrees(start,i-1)
            rights = self.creatTrees(i+1,end)
            for left in lefts:
                for right in rights:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    result.append(root)
        return result
        
