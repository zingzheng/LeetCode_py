##Remove Linked List Elements
##Remove all elements from a linked list of integers that have value val.
##
##2015年6月11日  AC
##zss

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        if not head:
            return head
        cur = head
        while cur:
            if head.val == val:
                head = head.next
                cur = head
            elif cur.val == val:
                cur = cur.next
                pre.next = cur
            else:
                pre = cur
                cur = cur.next
        return head
