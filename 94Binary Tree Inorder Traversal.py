##Binary Tree Inorder Traversal
##Given a binary tree, return the inorder traversal of its nodes' values.
##
##2015年8月12日   AC
##zss
##

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def inorderTraversal(self, root):
        result = []
        stack = []
        if not root: return result
        stack.append(root)
        while stack:
            if stack[-1].left:
                stack.append(stack[-1].left)
                stack[-2].left = None
            else:
                node = stack.pop(-1)
                result.append(node.val)
                if node.right:
                    stack.append(node.right)
        return result
                

class Solution2:
    # @param {TreeNode} root
    # @return {integer[]}
    res=[]
    def inorderTraversal(self, root):
        self.res=[]
        self.reduce(root)
        return self.res
    def reduce(self,root):
        if root and root.left:self.reduce(root.left)
        if root:self.res.append(root.val)
        if root and root.right:self.reduce(root.right)
