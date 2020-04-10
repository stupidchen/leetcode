class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.stack) == 0:
            self.stack.append((x, x))
        else:
            min = self.getMin()
            if min < x:
                self.stack.append((x, min))
            else:
                self.stack.append((x, x))

    def pop(self):
        """
        :rtype: void
        """
        self.stack = self.stack[: -1]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]
