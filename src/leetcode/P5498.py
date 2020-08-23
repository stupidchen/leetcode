from functools import lru_cache


class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)
        s = [0] * (n + 1)
        for i in range(n):
            s[i + 1] = s[i] + stoneValue[i]

        @lru_cache(maxsize=None)
        def f(x, y):
            if x >= y:
                return 0

            c = s[y + 1] - s[x]
            r = 0
            for i in range(x, y):
                t = s[i + 1] - s[x]
                m = min(t, c - t)
                if t == m:
                    r = max(m + f(x, i), r)
                if c - t == m:
                    r = max(m + f(i + 1, y), r)
            return r

        return f(0, n - 1)


if __name__ == '__main__':
    print(Solution().stoneGameV([6, 2, 3, 4, 5, 5]))
