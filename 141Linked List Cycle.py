##Linked List Cycle
##Given a linked list, determine if it has a cycle in it.
##
##2015年8月17日 19:57:49  AC
##zss

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        s1=head
        s2=head
        while s1 and s2 and s2.next:
            s1 = s1.next
            s2 = s2.next.next
            if s1 == s2:
                return True
        return False
            
