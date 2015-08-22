##Min Stack
##Design a stack that supports push, pop, top,
##and retrieving the minimum element in constant time.
##    push(x) -- Push element x onto stack.
##    pop() -- Removes the element on top of the stack.
##    top() -- Get the top element.
##    getMin() -- Retrieve the minimum element in the stack.
##
##2015年8月18日 14:54:01 AC
##zss

class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.stack=[]
        self.minN=None
        

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack.append(x)
        if not self.minN or x<self.minN:
            self.minN=x
        

    # @return nothing
    def pop(self):
        x = self.stack.pop(-1)
        if x==self.minN and self.stack:
            self.minN=min(self.stack)
        if x==self.minN and not self.stack:
            self.minN=None
        

    # @return an integer
    def top(self):
        return self.stack[-1]
        

    # @return an integer
    def getMin(self):
        return self.minN
