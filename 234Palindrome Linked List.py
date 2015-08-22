##Palindrome Linked List
##Given a singly linked list, determine if it is a palindrome.
##
##2015年8月21日 17:14:44  AC
##zss

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stack=[]
        while head:
            stack.append(head)
            head=head.next
        i,j=0,len(stack)-1
        while i<=j:
            if stack[i].val!=stack[j].val:
                return False
            i+=1
            j-=1
        return True
                
