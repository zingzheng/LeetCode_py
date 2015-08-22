##Convert Sorted List to Binary Search Tree
##Given a singly linked list where elements are sorted in ascending order,
##convert it to a height balanced BST.

##2015年8月14日 09:07:12  AC
##zss

##Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

##Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {ListNode} head
    # @return {TreeNode}
    def sortedListToBST(self, head):
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return self.sortedArrayToBST(nums)


    def sortedArrayToBST(self, nums):
        if not nums: return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
        
