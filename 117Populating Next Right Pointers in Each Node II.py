##Populating Next Right Pointers in Each Node II
##Follow up for problem "Populating Next Right Pointers in Each Node".
##What if the given tree could be any binary tree? Would your previous solution still work?

##2015年8月26日 18:05:48 AC
##zss

# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:return
        node=root
        while node:
            down = None
            while node:
                if not down:
                    if node.left: down = node.left
                    elif node.right: down = node.right
                nex = node.next
                while nex:
                    if nex.left or nex.right:
                        break
                    nex=nex.next
                if node.left and node.right:
                    node.left.next = node.right
                    
                if node.left and not node.right and nex:
                    if nex.left:
                        node.left.next=nex.left
                    else:
                        node.left.next=nex.right
                if node.right and nex:
                    if nex.left:
                        node.right.next=nex.left
                    else:
                        node.right.next=nex.right
                node=nex
            node=down
            


class Test(object):
    def t(self):
        t1= TreeLinkNode(1)
        t2= TreeLinkNode(2)
        t3= TreeLinkNode(3)
        t4= TreeLinkNode(4)
        t5= TreeLinkNode(5)
        t1.left=t2
        t1.right=t3
        t2.right=t4
        t3.left=t5
        return t1
