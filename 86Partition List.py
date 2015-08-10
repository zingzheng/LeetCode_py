##Partition List
##Given a linked list and a value x,
##partition it such that all nodes less than x come before
##nodes greater than or equal to x.
##You should preserve the original relative order of the nodes
##in each of the two partitions.
##
##2015年7月24日  AC
##zss

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        if not head:
            return head
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        i=j=0
        while j<len(nodes):
            if nodes[j].val < x:
                node = nodes.pop(j)
                nodes.insert(i,node)
                i += 1
            j += 1
        for i in range(len(nodes)-1):
            print(nodes[i].val)
            nodes[i].next = nodes[i+1]
        nodes[-1].next = None
        return nodes[0]

##class Test:
##    def t(self,l):
##        l1 = ListNode(1)
##        l2 = ListNode(4)
##        l3 = ListNode(3)
##        l4 = ListNode(2)
##        l5 = ListNode(5)
##        l6 = ListNode(2)
##        l1.next = l2
##        l2.next = l3
##        l3.next = l4
##        l4.next = l5
##        l5.next = l6
##        return l1
