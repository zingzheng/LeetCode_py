##Implement Queue using Stacks
##Implement the following operations of a queue using stacks.
##    push(x) -- Push element x to the back of queue.
##    pop() -- Removes the element from in front of queue.
##    peek() -- Get the front element.
##    empty() -- Return whether the queue is empty.
##
##2015年8月21日 16:09:43  AC
##zss

class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        stack_back=[]
        while self.stack:
            stack_back.append(self.stack.pop(-1))
        if stack_back:
            stack_back.pop(-1)
        while stack_back:
            self.stack.append(stack_back.pop(-1))
        

    def peek(self):
        """
        :rtype: int
        """
        stack_back=[]
        while self.stack:
            stack_back.append(self.stack.pop(-1))
        if stack_back:
            r = stack_back[-1]
        else:
            r = None
        while stack_back:
            self.stack.append(stack_back.pop(-1))
        return r

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack)==0
