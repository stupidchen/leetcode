class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        r = 0
        t = x ^ y
        while t > 0:
            t -= t ^ (t & (t - 1))
            r += 1
        return r
