##Binary Tree Right Side View
##Given a binary tree, imagine yourself standing on the right side of it,
##return the values of the nodes you can see ordered from top to bottom.
##
##2015年8月19日 14:46:05  AC
##zss

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        result=[]
        values = self.levelOrder(root)
        for row in values:
            result.append(row[-1])
        return result

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
