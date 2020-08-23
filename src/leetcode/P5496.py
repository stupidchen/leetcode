class Solution:
    def maxCoins(self, piles):
        p = sorted(piles)
        r = 0
        n = len(p)
        for i in range(n // 3):
            r += p[n - ((i + 1) << 1)]
        return r
