from functools import lru_cache

MOD = 10 ** 9 + 7


class Solution:
    def ways(self, pizza, k):
        n = len(pizza)
        m = len(pizza[0])
        s = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(n):
            for j in range(m):
                s[i + 1][j + 1] = s[i][j + 1] + s[i + 1][j] - s[i][j] + (1 if pizza[i][j] == 'A' else 0)

        def count(x1, y1, x2, y2):
            return s[x2 + 1][y2 + 1] - s[x1][y2 + 1] - s[x2 + 1][y1] + s[x1][y1]

        @lru_cache(maxsize=None)
        def solve(x, y, z):
            c = count(x, y, n - 1, m - 1)
            if c < z + 1:
                return 0

            if z == 0:
                return 1

            r = 0
            for i in range(x, n - 1):
                if count(x, y, i, m - 1) != 0:
                    r = (r + solve(i + 1, y, z - 1)) % MOD

            for j in range(y, m - 1):
                if count(x, y, n - 1, j) != 0:
                    r = (r + solve(x, j + 1, z - 1)) % MOD
            return r

        return solve(0, 0, k - 1)


if __name__ == '__main__':
    print(Solution().ways(pizza=["A..", "AA.", "..."], k=3))
    print(Solution().ways(pizza=["A..", "AAA", "..."], k=3))
    print(Solution().ways(pizza=["A..", "A..", "..."], k=1))
