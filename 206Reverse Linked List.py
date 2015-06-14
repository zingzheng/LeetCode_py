##Reverse Linked List
##Reverse a singly linked list.
##
##2015年6月10日 AC
##zss

##Definition for singly-linked list.
##class ListNode:
##    def __init__(self, x):
##        self.val = x
##        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        pre = head
        cur = pre.next
        pre.next = None
        while cur != None:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre
            
