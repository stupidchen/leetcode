class FreqStack:

    def __init__(self):
        self.freq = {}
        self.stack = {}
        self.top = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.freq[x] = self.freq.setdefault(x, 0) + 1
        f = self.freq[x]
        self.stack.setdefault(f, []).append(x)
        self.top = max(self.top, f)

    def pop(self):
        """
        :rtype: int
        """
        i = self.top
        while i > 0 and len(self.stack[i]) == 0:
            i -= 1
        ret = None
        if len(self.stack[i]) > 0:
            ret = self.stack[i][-1]
            self.stack[i] = self.stack[i][:-1]
        self.top = i
        return ret


if __name__ == '__main__':
    obj = FreqStack()
    obj.push(1)
    obj.push(0)
    obj.push(0)
    obj.push(1)
    obj.push(5)
    obj.push(4)
    obj.push(1)
    obj.push(5)
    obj.push(1)
    obj.push(6)
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())
    print(obj.pop())
