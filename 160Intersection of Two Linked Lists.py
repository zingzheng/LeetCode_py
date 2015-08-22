##Intersection of Two Linked Lists
##Write a program to find the node at which the intersection
##of two singly linked lists begins.
##
##2015年8月18日 15:14:59  AC
##zss

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:return None
        la=lb=1
        ha,hb=headA,headB
        while ha.next:
            ha=ha.next
            la+=1
        while hb.next:
            hb=hb.next
            lb+=1
        if ha!=hb:return None
        if la>=lb:
            i=0
            for i in range(la-lb):
                headA=headA.next
        else:
            i=0
            for i in range(lb-la):
                headB=headB.next
        while headA!=headB:
            headA=headA.next
            headB=headB.next
        return headA
                
            
