class Cashier:

    def __init__(self, n, discount, products, prices):
        self.prices = {products[i]: prices[i] for i in range(len(products))}
        self.n, self.discount = n, discount
        self.c = 0

    def getBill(self, product, amount):
        p = 0
        for i in range(len(product)):
            p += self.prices[product[i]] * amount[i]
        self.c = (self.c + 1) % self.n
        if self.c == 0:
            p = p * (1 - self.discount / 100)
        return p


# This kind of input is not supported by tester temporarily
if __name__ == '__main__':
    cashier = Cashier(3, 50, [1, 2, 3, 4, 5, 6, 7], [100, 200, 300, 400, 300, 200, 100])
    print(cashier.getBill([1, 2], [1, 2]))
    print(cashier.getBill([3, 7], [10, 10]))
    print(cashier.getBill([1, 2, 3, 4, 5, 6, 7], [1, 1, 1, 1, 1, 1, 1]))
    print(cashier.getBill([4], [10]))
    print(cashier.getBill([7, 3], [10, 10]))
    print(cashier.getBill([7, 5, 3, 1, 6, 4, 2], [10, 10, 10, 9, 9, 9, 7]))
    print(cashier.getBill([2, 3, 5], [5, 3, 2]))
