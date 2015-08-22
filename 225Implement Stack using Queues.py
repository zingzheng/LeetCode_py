##Implement Stack using Queues
##Implement the following operations of a stack using queues.
##
##    push(x) -- Push element x onto stack.
##    pop() -- Removes the element on top of the stack.
##    top() -- Get the top element.
##    empty() -- Return whether the stack is empty.
##
##Notes:
##
##    You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
##    Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
##    You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
##
##2015年8月19日 17:02:13  AC
##zss



class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.q=[]

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.q.append(x)

    # @return nothing
    def pop(self):
        tmp = None
        q_back=[]
        while len(self.q)>1:
            q_back.append(self.q.pop(0))
        self.q=q_back[::]
        

    # @return an integer
    def top(self):
        tmp = None
        q_back=[]
        while not self.empty():
            tmp = self.q.pop(0)
            q_back.append(tmp)
        self.q=q_back[::]
        return tmp
        

    # @return an boolean
    def empty(self):
        return len(self.q)==0
