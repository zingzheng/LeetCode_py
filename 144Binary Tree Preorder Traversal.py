##Binary Tree Preorder Traversal
##Given a binary tree, return the preorder traversal of its nodes' values.
##
##2015年8月17日 20:27:07  AC
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
    def preorderTraversal(self, root):
        self.result=[]
        self.preOrder(root)
        return self.result
        
    def preOrder(self,root):
        if root:
            self.result.append(root.val)
            if root.left:
                self.preOrder(root.left)
            if root.right:
                self.preOrder(root.right)

    def preOrderIter(self,root):
        result=[]
        stack=[]
        if not root:return result
        stack.append(root)
        while stack:
            head = stack.pop(-1)
            result.append(head.val)
            if head.right:
                stack.append(head.right)
            if head.left:
                stack.append(head.left)
        return result


