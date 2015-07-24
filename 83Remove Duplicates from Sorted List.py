##Remove Duplicates from Sorted List
##Given a sorted linked list, delete all duplicates
##such that each element appear only once.
##
##2015年7月14日   AC
##zss
##

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if not head:
            return head
        c = head
        while c.next:
            n = c.next
            if n.val == c.val:
                c.next = n.next
            else:
                c = c.next
        return head

##class Test:
##    def t(self):
##        l1 = ListNode(1)
##        l2 = ListNode(1)
##        l3 = ListNode(2)
##        l4 = ListNode(3)
##        l5 = ListNode(3)
##        l1.next = l2
##        l2.next = l3
##        l3.next = l4
##        l4.next = l5
##        return l1
        
