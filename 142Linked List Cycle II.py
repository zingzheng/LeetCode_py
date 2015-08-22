##Linked List Cycle II
##Given a linked list, return the node where the cycle begins.
##If there is no cycle, return null.
##
##2015年8月17日 20:02:20 AC
##zss
##可用证明 相遇的节点 和 起始 同时开始相遇点为入口

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        s1 = self.hasCycle(head)
        if s1:
            while s1 and head:
                if s1==head:
                    return head
                s1=s1.next
                head=head.next
        return None
        
    def hasCycle(self,head):
        s1=head
        s2=head
        while s1 and s2 and s2.next:
            s1 = s1.next
            s2 = s2.next.next
            if s1 == s2:
                return s1
        return None
