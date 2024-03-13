import math
from functools import lru_cache


class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        @lru_cache(maxsize=None)
        def f(n):
            if n <= 0:
                return 0
            if n == 1:
                return int(x == 1)
            m = int(math.log2(n))
            t = n - (1 << m)
            ret = f(n - t - 1) + f(t) + (int((m + 1) % x == 0) * (t + 1))
            return ret


        lo = 0
        if k >= 10 ** 10:
            hi = int(0.6 * k)
        else:
            hi = 10 ** 10
        res = -1
        while lo <= hi:
            mid = (lo + hi) >> 1
            t = f(mid)
            if t <= k:
                res = max(res, mid)
            if t > k:
                hi = mid - 1
            else:
                lo = mid + 1
        return res


if __name__ == '__main__':
    r = Solution().findMaximumNumber(10 ** 9, 8)
    print(r)
