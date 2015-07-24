##Remove Duplicates from Sorted List II
##Given a sorted linked list, delete all nodes that have duplicate numbers,
##leaving only distinct numbers from the original list.

##2015年7月14日   AC
##zss

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if not head:
            return head
        nodes1 = []
        nodes2 = []
        
        c = head
        while c:

            if not nodes1 or nodes1[-1].val != c.val:
                if not nodes2 or nodes2[-1].val != c.val:
                    nodes2.append(c)
                else:
                    nodes2.pop(-1)
                    nodes1.append(c)
            else:
                nodes1.append(c)
                
            c = c.next
        for i in range(len(nodes2)-1):
            nodes2[i].next = nodes2[i+1]
        if nodes2:
            nodes2[-1].next = None
            return nodes2[0]
        else:
            return None


class Test:
    def t(self):
        l1 = ListNode(1)
        l2 = ListNode(2)
        l3 = ListNode(2)
        l4 = ListNode(3)
        l1.next = l2
        l2.next = l3
        l3.next = l4
        return l1
