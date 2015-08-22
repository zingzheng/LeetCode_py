##Sort List
##Sort a linked list in O(n log n) time using constant space complexity.
##
##2015年8月18日 09:36:45
##zss

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def sortList(self, head):
        if not head or not head.next:return head
        head2=self.cutList(head)
        return self.mergeTwoLists(self.sortList(head),self.sortList(head2))


    def cutList(self,head):
        s1=head
        s2=head
        while s2.next and s2.next.next:
            s1=s1.next
            s2=s2.next.next
        head2 = s1.next
        s1.next=None
        return head2
        

    def mergeTwoLists(self, l1, l2):
        if not l1:return l2
        if not l2:return l1
        l1c,l2c = l1,l2
        l1n,l2n = l1.next,l2.next
        if l1c.val <= l2c.val:
            head = l1c
            l1c = l1n
            if l1n:
                l1n = l1n.next
        else:
            head = l2c
            l2c = l2n
            if l2n:
                l2n = l2n.next
        c = head
        while l1c or l2c:
            if l1c and l2c:
                if l1c.val<=l2c.val:
                    c.next = l1c
                    c = c.next
                    l1c = l1n
                    if l1n:
                        l1n = l1n.next
                else:
                    c.next = l2c
                    c =c.next
                    l2c = l2n
                    if l2n:
                        l2n = l2n.next
            elif l1c:
                c.next = l1c
                break
            elif l2c:
                c.next = l2c
                break
        return head

        
