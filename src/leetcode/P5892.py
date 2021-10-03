from collections import Counter
from functools import cache
from typing import List


class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        stones = [stone % 3 for stone in stones]
        c = Counter(stones)

        @cache
        def f(c0, c1, c2, a):
            if c0 + c1 + c2 == 0:
                return not a
            cs = s - c1 - (c2 << 1)
            r = False
            if c0 > 0:
                if cs % 3 != 0:
                    r = r or not f(c0 - 1, c1, c2, not a)
                    if r:
                        return True
            if c1 > 0:
                if (cs + 1) % 3 != 0:
                    r = r or not f(c0, c1 - 1, c2, not a)
                    if r:
                        return True
            if c2 > 0:
                if (cs + 2) % 3 != 0:
                    r = r or not f(c0, c1, c2 - 1, not a)
                    if r:
                        return True
            return r

        c = [c[0] % 100, c[1] % 100, c[2] % 100]
        s = c[1] + (c[2] << 1)
        return f(c[0], c[1], c[2], True)


# c0 = 0: c[1]
#

if __name__ == '__main__':
    print(Solution().stoneGameIX([15, 20, 10, 13, 14, 15, 5, 2, 3]))
    print(Solution().stoneGameIX([20, 3, 20, 17, 2, 12, 15, 17, 4]))
