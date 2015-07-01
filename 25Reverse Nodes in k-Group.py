##Reverse Nodes in k-Group
##Given a linked list, reverse the nodes of a linked list k at a time
##and return its modified list.
##If the number of nodes is not a multiple of k
##then left-out nodes in the end should remain as it is.
##You may not alter the values in the nodes, only nodes itself may be changed.
##Only constant memory is allowed.
##
##2015年6月30日  AC
##zss

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        if k == 1:
            return head
        h = ListNode(0)
        h.next = head
        c = h
        it = head
        buffer = []
        while c:
            f = 0
            buffer.clear()
            for i in range(k):
                if it:
                    buffer.append(it)
                    it = it.next
                else:
                    f = 1
                    break
            if len(buffer) == k:
                for i in range(k-1):
                    buffer[i+1].next = buffer[i]
            if f:
                if buffer:
                    c.next = buffer[0]
                c = None
            else:
                c.next = buffer[-1]
                c = buffer[0]
                c.next = None
        return h.next

class Test():
    def t(self):
        t1 = ListNode(1)
        t2 = ListNode(2)
        t3 = ListNode(3)
        t4 = ListNode(4)
        t5 = ListNode(5)
        t1.next = t2
        t2.next =t3
        t3.next = t4
        t4.next = t5
        return t1
            
