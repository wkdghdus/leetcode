class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minimum = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if self.minimum:
            self.minimum.append(min(self.minimum[-1], val))
        else:
            self.minimum.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        self.minimum.pop()
        return self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        
        return self.minimum[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()