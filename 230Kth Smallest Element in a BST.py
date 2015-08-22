##Kth Smallest Element in a BST
##Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
##Note:
##You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
##
##2015年8月21日 15:23:55  AC
##zss

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack=[]
        node = root
        while node:
            stack.append(node)
            node = node.left
        x=1
        while stack and x<=k:
            node = stack.pop()
            x+=1
            right = node.right
            while right:
                stack.append(right)
                right=right.left
        return node.val
        
        
