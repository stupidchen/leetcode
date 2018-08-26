class FreqStack:

    def __init__(self):
        self.num = []
        self.val = []
        self.link = {}
        self.freq = {}
        self.count = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x not in self.freq or self.freq[x] >= len(self.num):
            self.freq[x] = len(self.num)
            self.num.append(1)
            self.val.append(x)
            self.link[x] = [self.count]
        else:
            self.num[self.freq[x]] += 1
            self.link[x].append(self.count)
        i = self.freq[x]
        while i > 0 and (self.num[i] > self.num[i - 1] or
                         (self.num[i] == self.num[i - 1] and self.link[self.val[i]][-1] > self.link[self.val[i - 1]][-1])):
            self.num[i], self.num[i - 1] = self.num[i - 1], self.num[i]
            self.val[i], self.val[i - 1] = self.val[i - 1], self.val[i]
            self.freq[self.val[i - 1]], self.freq[self.val[i]] = self.freq[self.val[i]], self.freq[self.val[i - 1]]
            i -= 1
        self.count += 1

    def pop(self):
        """
        :rtype: int
        """
        l = len(self.num)
        if l == 0:
            return

        ret = self.val[0]
        self.num[0] -= 1
        i = 0
        self.link[ret] = self.link[ret][:-1]
        ll = len(self.link[ret])
        while i < l - 1 and (self.num[i] < self.num[i + 1] or
                             (ll > 0 and self.num[i] == self.num[i + 1] and self.link[self.val[i + 1]][-1] > self.link[self.val[i]][-1])):
            self.num[i], self.num[i + 1] = self.num[i + 1], self.num[i]
            self.val[i], self.val[i + 1] = self.val[i + 1], self.val[i]
            self.freq[self.val[i]], self.freq[self.val[i + 1]] = self.freq[self.val[i + 1]], self.freq[self.val[i]]
            i += 1
        if self.num[i] == 0:
            del self.freq[ret]
            self.num = self.num[:i]
            self.val = self.val[:i]

        self.count -= 1
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
