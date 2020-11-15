class OrderedStream:

    def __init__(self, n: int):
        self.a = [''] * n
        self.p = 0
        self.n = n

    def insert(self, id: int, value: str):
        id -= 1
        self.a[id] = value
        if id == self.p:
            r = [self.a[id]]
            i = id
            for i in range(id + 1, self.n):
                if self.a[i] != '':
                    r.append(self.a[i])
                else:
                    break
            self.p = i
            return r

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)
