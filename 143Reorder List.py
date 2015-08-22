##Reorder List
##Given a singly linked list L: L0→L1→…→Ln-1→Ln,
##reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
##You must do this in-place without altering the nodes' values.
##
##2015年8月17日 20:11:28  AC
##zss

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):
        if not head or not head.next:return
        s1=head
        s2=head
        ##cut
        while s2 and s2.next:
            s1=s1.next
            s2=s2.next.next
        head2 = s1.next
        s1.next=None
        ##reverse
        head2 = self.reverseList(head2)
        ##merge
        while head2:
            p1=head.next
            head.next=head2
            head=p1
            p2=head2.next
            head2.next=head
            head2=p2
            

    ##206 Reverse Linked List
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
