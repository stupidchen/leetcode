class StockSpanner:

    def __init__(self):
        self.s = []

    def next(self, price):
        r = 1
        while self.s and self.s[-1][0] <= price:
            r += self.s.pop()[1]
        self.s.append([price, r])

        return r


if __name__ == '__main__':
    s = StockSpanner()
    print(s.next(100))
    print(s.next(80))
    print(s.next(60))
    print(s.next(70))
    print(s.next(60))
    print(s.next(75))
    print(s.next(85))

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
