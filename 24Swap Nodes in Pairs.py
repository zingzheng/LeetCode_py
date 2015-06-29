##Swap Nodes in Pairs
##Given a linked list, swap every two adjacent nodes and return its head.
##For example,
##Given 1->2->3->4, you should return the list as 2->1->4->3
##
##2015年6月29日  AC
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
    def swapPairs(self, head):
        if not (head and head.next):
            return head
        h = ListNode(0)
        h.next = head
        c,n = h,head
        while n and n.next:
            c.next = n.next
            c = c.next
            n.next = c.next
            c.next = n
            c = n
            n = n.next
        return h.next

class Test():
    def t(self):
        l1 = ListNode(1)
        l2 = ListNode(2)
        l3 = ListNode(3)
        l4 = ListNode(4)
        l5 = ListNode(5)
        l1.next = l2
        l2.next = l3
        #l3.next = l4
        #l4.next = l5
        return l1
