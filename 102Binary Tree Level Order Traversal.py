##Binary Tree Level Order Traversal
##Given a binary tree, return the level order traversal of its nodes' values
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
    # @return {integer[][]}
    def levelOrder(self, root):
        if not root :return []
        levels = [[root]]
        values = [[root.val]]
        for level in levels:
            newLevel = []
            newValue = []
            for node in level:
                if node.left:
                    newLevel.append(node.left)
                    newValue.append(node.left.val)
                if node.right:
                    newLevel.append(node.right)
                    newValue.append(node.right.val)
            if newLevel:
                levels.append(newLevel)
                values.append(newValue)
        return values
        
        
    
