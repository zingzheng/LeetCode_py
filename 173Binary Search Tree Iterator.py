##Binary Search Tree Iterator
##Implement an iterator over a binary search tree (BST).
##Your iterator will be initialized with the root node of a BST.
##Calling next() will return the next smallest number in the BST.
##Note: next() and hasNext() should run in average O(1) time
##and uses O(h) memory, where h is the height of the tree.
##
##2015年8月19日 08:46:23  AC
##zss


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack=[]
        while root:
            self.stack.append(root)
            root=root.left
        

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.stack)!=0
        

    # @return an integer, the next smallest number
    def next(self):
        if self.stack:
            root=self.stack.pop(-1)
            rig = root.right
            while rig:
                self.stack.append(rig)
                rig=rig.left
            return root.val
        return None
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
