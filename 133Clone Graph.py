##Clone Graph
##Clone an undirected graph.
##Each node in the graph contains a label and a list of its neighbors.
##
##2015年8月17日 15:24:38  AC
##zss

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    dic={}
    def cloneGraph(self, node):
        if not node:return None
        root = UndirectedGraphNode(node.label)
        self.dic[node.label]=root
        for n in node.neighbors:
            if n.label in self.dic:
                root.neighbors.append(self.dic[n.label])
            else:
                root.neighbors.append(self.cloneGraph(n))
        return root

class Test:
    def t(self):
        n2 = UndirectedGraphNode(2)
        n2.neighbors.append(n2)
        n1 = UndirectedGraphNode(1)
        n1.neighbors.append(n2)
        n0 = UndirectedGraphNode(0)
        n0.neighbors.append(n1)
        return n0




        
        
