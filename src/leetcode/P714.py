from math import inf


class Solution:
    def maxProfit(self, prices, fee):
        d = []
        for i in range(1, len(prices)):
            d.append(prices[i] - prices[i - 1])

        n = len(d)
        f, g = [-inf] * (n + 1), [0] * (n + 1)
        for i in range(n):
            f[i + 1] = d[i] + max(f[i], g[i] - fee)
            g[i + 1] = max(g[i], f[i])
        return max(g[n], f[n])


if __name__ == '__main__':
    print(Solution().maxProfit(prices=[1, 3, 7, 5, 10, 3], fee=3))
