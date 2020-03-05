class Solution:
    def arrangeCoins(self, n: int) -> int:
        r = 1
        while n - r >= 0:
            n -= r
            r += 1
        return r - 1
