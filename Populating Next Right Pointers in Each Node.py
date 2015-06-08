#Populating Next Right Pointers in Each Node
#Populate each next pointer to point to its next right node.
#If there is no next right node,the next pointer should be set to NULL.

#2015年6月8日 AC
#zss

# Definition for binary tree with next pointer.
##class TreeLinkNode:
##     def __init__(self, x):
##         self.val = x
##         self.left = None
##         self.right = None
##         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        nodeList = [root]
        tag = 1
        i = 1
        while len(nodeList):
            treeNode = nodeList.pop(0)
            if  treeNode and treeNode.left:
                nodeList.extend([treeNode.left,treeNode.right])
            if i == tag:
                i = 1
                tag *= 2
            else:
                if len(nodeList):
                    treeNode.next = nodeList[0]
                i += 1
            
