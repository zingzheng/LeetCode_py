##297. Serialize and Deserialize Binary Tree
##
##2016年4月4日 15:20:40
##zss

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Test:
    def t(self):
        t1 = TreeNode('1')
        t2 = TreeNode('2')
        t3 = TreeNode('3')
        t4 = TreeNode('4')
        t5 = TreeNode('5')
        t1.left=t2
        t1.right=t3
        t2.left=t4
        t2.right=t5
        c = Codec()
        data = c.serialize(t1)
        print(data)
        root = c.deserialize(data)
        return root
        


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:return None
        q =[root]
        i,endIndex=0,1
        while i<endIndex:
            if q[i]:
                q.append(q[i].left)
                q.append(q[i].right)
                endIndex+=2;
            i+=1
        res=[]
        for node in q:
            if node:
                res.append(str(node.val))
            else:
                res.append("#")
        return ','.join(res)
                
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:return None
        values = data.split(',')
        nodes = [None]*len(values)
        count=0
        for i in range(len(values)):
            if values[i] != '#':
                nodes[i] = TreeNode(int(values[i]))
        for i in range(len(nodes)):
            if not nodes[i]:
                count+=1
            else:
                nodes[i].left=nodes[2*(i-count)+1]
                nodes[i].right=nodes[2*(i-count)+2]
        return nodes[0]
            


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


