class Solution:
    def minOperations(self, n: int) -> int:
        a = [(i << 1) + 1 for i in range(n)]
        r = 0
        for i in range(n >> 1):
            r += ((a[-(i + 1)] + a[i]) >> 1) - a[i]
        return r
