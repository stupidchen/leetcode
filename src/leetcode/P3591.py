from functools import lru_cache


class Solution:
    def countArrangement(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def find(i, X):
            if i == 1:
                return 1
            r = 0
            for x in X:
                if i % x == 0 or x % i == 0:
                    r += find(i - 1, tuple(set(X) - {x}))
            return r

        return find(n, tuple(range(1, n + 1)))
