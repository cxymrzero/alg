# -*- coding: utf-8 -*-
class MinStack:
    """
    第二个栈维护第一个栈中的最小值, 每次入栈不小于s2栈顶的元素都要压入s2
    """
    def __init__(self):
        self.s1 = []
        self.s2 = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.s1.append(x)
        if len(self.s2) == 0 or x <= self.s2[-1]:
            self.s2.append(x)
        return x

    # @return nothing
    def pop(self):
        x = self.s1.pop()
        if x == self.s2[-1]:
            self.s2.pop()

    # @return an integer
    def top(self):
        return self.s1[-1]

    # @return an integer
    def getMin(self):
        return self.s2[-1]

s = MinStack()
s.push(1)
s.push(2)
s.push(3)
print s.top()
print s.s1
print s.getMin()
s.pop()
print s.s1