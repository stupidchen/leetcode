import math
from functools import lru_cache


class Solution:
    def minDays(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def f(x, o=0):
            if o >= 3:
                return math.inf
            if x <= 2:
                return x
            t = f(x - 1, o + 1)
            if x & 1 == 0:
                t = min(t, f(x // 2))
            if x % 3 == 0:
                t = min(t, f(x // 3))
            return t + 1

        return f(n)
