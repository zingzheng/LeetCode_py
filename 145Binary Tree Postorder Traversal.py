##Binary Tree Postorder Traversal
##Given a binary tree, return the postorder traversal of its nodes' values.
##
##2015年8月17日 20:37:59  AC
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
    def postorderTraversal(self, root):
        self.result=[]
        self.postOrder(root)
        return self.result
        
    def postOrder(self,root):
        if root:
            if root.left:
                self.postOrder(root.left)
            if root.right:
                self.postOrder(root.right)
            self.result.append(root.val)

    def postOrderIter(self,root):
        result=[]
        stack=[]
        if not root:return result
        stack.append(root)
        while stack:
            top = stack[-1]
            if not top.left and not top.right:
                result.append(top.val)
                stack.pop(-1)
            else:
                if top.right:
                    stack.append(top.right)
                    top.right=None
                if top.left:
                    stack.append(top.left)
                    top.left=None
        return result
