##Count Complete Tree Nodes
##Given a complete binary tree, count the number of nodes.
##
##2015年6月9日  TLE
##zss

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        return self.counter(root)


    def leftDeep(self, root):
        i = 0
        node = root
        while node and node.left:
            i += 1
            node = node.left
        return i

    def rightDeep(self, root):
        i = 0
        node = root
        while node and node.right:
            i += 1
            node = node.right
        return i

    def counter(self, root):
        if not root:
            return 0
        else:
            l = self.leftDeep(root)+1
            r = self.rightDeep(root)+1
            print(l)
            print(r)
            if l == r:
                return 2 ** l - 1
            else:
                return self.counter(root.left) + self.counter(root.right) + 1
            
