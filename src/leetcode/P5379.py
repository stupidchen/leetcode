from functools import lru_cache


class Solution:
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)
        f = [0] * (n + 1)
        for i in range(n):
            f[i + 1] = f[i] + stoneValue[i]

        def p_sum(l, r):
            if r > n:
                r = f[-1]
            else:
                r = f[r]
            if l > n:
                l = f[-1]
            else:
                l = f[l]
            return r - l

        @lru_cache(maxsize=None)
        def solve(c):
            if c >= n:
                return 0

            t, m = 0, float('-inf')
            for i in range(3):
                if c + i < n:
                    t += stoneValue[c + i]
                    f = solve(c + i + 1)
                    m = max(t + p_sum(c + i + 1, n) - f, m)
                else:
                    break

            return m

        a = solve(0)
        s = p_sum(0, n)
        if a > s - a:
            return 'Alice'
        elif a == s - a:
            return 'Tie'
        else:
            return 'Bob'


if __name__ == '__main__':
    print(Solution().stoneGameIII(([1, 2, 3, -1, -2, -3, 7])))
