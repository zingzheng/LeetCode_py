##Path Sum II
##Given a binary tree and a sum, find all root-to-leaf paths
##where each path's sum equals the given sum.
##
##2015年8月14日 11:24:05  AC
##zss

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {integer[][]}
    def pathSum(self, root, sum):
        self.result = []
        self.reduce(root,sum,[])
        return self.result

    def reduce(self,root,sum,nodes0):
        nodes = nodes0[::]
        if not root:return
        else:
            nodes.append(root.val)
            sum-=root.val
            if sum==0 and not root.left and not root.right:
                self.result.append(nodes)
            elif sum!=0 and not root.left and not root.right:
                return
            elif root.left and not root.right:
                self.reduce(root.left,sum,nodes)
            elif root.right and not root.left:
                self.reduce(root.right,sum,nodes)
            elif root.right and root.left:
                self.reduce(root.left,sum,nodes)
                self.reduce(root.right,sum,nodes)
