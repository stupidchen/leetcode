class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        r = 0
        for i in range(n):
            r = r ^ (start + (i << 1))
        return r
