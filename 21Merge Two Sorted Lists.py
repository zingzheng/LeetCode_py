##Merge Two Sorted Lists
##Merge two sorted linked lists and return it as a new list.
##The new list should be made by splicing together the nodes of the first two lists.
##2015年6月29日  AC
##zss

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
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


##class Test:
##    def t(self):
##        l10 = ListNode(1)
##        l11 = ListNode(3)
##        #l10.next = l11
##        l20 = ListNode(0)
##        l21 = ListNode(2)
##        #l22 = ListNode(4)
##        #l23 = ListNode(6)
##        #l20.next = l21
##        #l21.next = l22
##        #l22.next = l23
##        return l10,l20
