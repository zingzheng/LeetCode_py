##Rotate List
##Given a list, rotate the list to the right by k places, where k is non-negative.
##
##2015年7月7日
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
    def rotateRight(self, head, k):
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        if nodes:
            k%=len(nodes)
        left = nodes[:len(nodes)-k]
        right = nodes[len(nodes)-k:]
        if right and left:
            right[-1].next = left[0]
            left[-1].next=None
            return right[0]
        elif right and not left:
            right[-1].next=None
            return right[0]
        elif left and not right:
            left[-1].next=None
            return left[0]
        else:
            return head
            
                
