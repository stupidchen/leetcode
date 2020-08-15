class Solution:
    def finalPrices(self, prices):
        n = len(prices)
        r = [price for price in prices]
        for i in range(n):
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    r[i] -= prices[j]
                    break
        return r
