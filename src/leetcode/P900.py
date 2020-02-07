class RLEIterator:

    def __init__(self, A):
        self.a = A
        self.s = (0, 0)

    def next(self, n):
        e, p = self.s
        while e < len(self.a) and self.a[e] - p < n:
            n -= self.a[e] - p
            e += 2
            p = 0
        if e >= len(self.a):
            p += n
            self.s = (e, p)
            return -1
        else:
            p += n
            self.s = (e, p)
            return self.a[e + 1]


if __name__ == '__main__':
    i = RLEIterator([3, 8, 0, 9, 2, 5])
    print(i.next(2))
    print(i.next(1))
    print(i.next(1))
    print(i.next(1))
    print(i.next(1))
    print(i.next(1))
    print(i.next(1))
    print(i.next(1))
    print(i.next(1))
    print(i.next(1))
    print(i.next(1))
# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)