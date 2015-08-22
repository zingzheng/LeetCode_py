##Binary Tree Level Order Traversal II
##Given a binary tree, return the bottom-up level order traversal of its nodes' values.
##
##2015年8月14日 08:48:39  AC
##zss

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrderBottom(self, root):
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
                values.insert(0,newValue)
        return values
