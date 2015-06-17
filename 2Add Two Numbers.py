##Add Two Numbers
##You are given two linked lists representing two non-negative numbers.
##The digits are stored in reverse order and each of their nodes contain
##a single digit. Add the two numbers and return it as a linked list.
##
##2015年6月17日 AC
##zss
##

##Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        h1 = l1
        h2 = l2
        h3 = ListNode(-1)
        l3 = h3
        flag = 0
        while h1 or h2:
            n1 = n2 = 0
            if h1:
                n1 = h1.val
                h1 = h1.next
            if h2:
                n2 = h2.val
                h2 = h2.next
            node = ListNode((n1+n2+flag)%10)
            if n1+n2+flag >= 10:
                flag = 1
            else:
                flag = 0
            h3.next = node
            h3 = h3.next
        if flag == 1:
            node = ListNode(1)
            h3.next = node
        return l3.next

        
        
        
            
