##Insertion Sort List
##Sort a linked list using insertion sort.
##
##2015年8月18日 08:53:49 AC
##zss

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head == None or head.next == None:
            return head
        h = ListNode(0)
        h.next = head
        cur = head
        while cur.next:
            if cur.next.val < cur.val:
                pre = h
                while pre.next.val < cur.next.val:
                    pre = pre.next
                temp = cur.next
                cur.next = temp.next
                temp.next = pre.next
                pre.next = temp
            else:
                cur = cur.next
        return h.next

