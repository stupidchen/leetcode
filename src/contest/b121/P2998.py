import math
from functools import lru_cache


class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        @lru_cache(maxsize=None)
        def f(t, d):
            if y >= t:
                return y - t

            if t == 0:
                return math.inf

            res = t - y
            if t % 11 == 0:
                if abs(t // 11 - y) < min(abs(t // 11 - 1 - y) + 11, abs(t // 11 + 1 - y) + 11):
                    res = min(res, f(t // 11, d) + 1)

            if t % 5 == 0:
                if abs(t // 5 - y) < min(abs(t // 5 - 1 - y) + 5, abs(t // 5 + 1 - y) + 5):
                    res = min(res, f(t // 5, d) + 1)

            if d <= 22:
                res = min(res, min(f(t + 1, d + 1) + 1, f(t - 1, d + 1) + 1))
            return res

        return f(x, 0)


if __name__ == '__main__':
    r = Solution().minimumOperationsToMakeEqual(1000, 57)
    print(r)
