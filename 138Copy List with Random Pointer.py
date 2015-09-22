##Copy List with Random Pointer
##A linked list is given such that each node contains an additional
##random pointer which could point to any node in the list or null.
##Return a deep copy of the list.
##
##2015年9月22日 10:41:33  AC
##zss
##把新节点附在原节点后

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:return head
        node=head
        while node:
            copyNode = RandomListNode(node.label)
            copyNode.random = node.random
            copyNode.next = node.next
            node.next = copyNode
            node = node.next.next

        node=head
        while node:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next

        phead=RandomListNode(0)
        phead.next=head
        newlist=phead
        node=head

        while node:
            phead.next=node.next
            node.next=phead.next.next
            phead=phead.next
            node=node.next
        return newlist.next
        
