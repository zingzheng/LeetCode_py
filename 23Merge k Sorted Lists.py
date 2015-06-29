##Merge k Sorted Lists
##2015年6月29日   AC
##zss

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        nodes = []
        for l in lists:
            while l:
                nodes.append(l)
                l = l.next
        if not nodes:
            return
        nodes.sort(key=lambda node:node.val)
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]
        nodes[-1].next = None
        return nodes[0]


