##328. Odd Even Linked List
##Given a singly linked list, group all odd nodes together followed by the even nodes.
##Please note here we are talking about the node number and not the value in the nodes.
##You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
##
##zss  AC
##2016年2月28日

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:return head
        h1=c1=head
        h2=c2=head.next

        while True:
            if not c1.next or not c1.next.next:
                break
            c1.next=c1.next.next
            c1=c1.next
            c2.next=c2.next.next
            c2=c2.next
        c1.next=h2
        if c2:
            c2.next=None
        return h1;
