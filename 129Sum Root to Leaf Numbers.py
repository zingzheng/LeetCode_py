##Sum Root to Leaf Numbers
##Given a binary tree containing digits from 0-9 only,
##each root-to-leaf path could represent a number.
##An example is the root-to-leaf path 1->2->3 which represents the number 123.
##Find the total sum of all root-to-leaf numbers.
##
##2015年8月17日 09:31:44 AC
##zss

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def sumNumbers(self, root):
        self.sum=0
        self.reduce(root,0)
        return self.sum

    def reduce(self,root,n):
        if not root:
            self.sum+=n
        elif not root.left and not root.right:
            n = 10*n+root.val
            self.sum+=n
        else:
            n = 10*n+root.val
            if root.left:self.reduce(root.left,n)
            if root.right:self.reduce(root.right,n)
