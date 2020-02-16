class ProductOfNumbers:

    def __init__(self):
        self.p = [[0] * 101]

    def add(self, num: int) -> None:
        t = [i for i in self.p[-1]]
        t[num] += 1
        self.p.append(t)

    def getProduct(self, k: int) -> int:
        r = 1
        t, l = self.p[-1], self.p[-k - 1]
        for i in range(101):
            r = r * (i ** (t[i] - l[i]))
            if r == 0:
                break
        return r


# This kind of input is not supported by tester temporarily
if __name__ == '__main__':
    obj = ProductOfNumbers()
    obj.add(3)
    obj.add(0)
    obj.add(2)
    obj.add(5)
    obj.add(4)
    print(obj.getProduct(2))
    print(obj.getProduct(3))
    print(obj.getProduct(4))
    obj.add(8)
    print(obj.getProduct(2))
