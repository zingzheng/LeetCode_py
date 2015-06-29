##Remove Nth Node From End of List
##Given a linked list, remove the nth node from the end of list
##and return its head.
##
##2015年6月29日  AC
##zss

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        pre = ListNode(0)
        pre.next = head
        cur = head
        head = pre
        while cur != None:
            future = cur
            for i in range(n-1):
                future = future.next
            if future.next == None:
                pre.next = cur.next
                return head.next
            else:
                pre = cur
                cur = cur.next

##class Test:
##    def t(self):
##        l1 = ListNode(1)
##        l2 = ListNode(2)
##        l3 = ListNode(3)
##        l4 = ListNode(4)
##        l5 = ListNode(5)
##        l1.next =l2
##        l2.next = l3
##        l3.next = l4
##        l4.next = l5
##        return l1
