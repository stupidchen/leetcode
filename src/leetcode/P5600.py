from functools import lru_cache


class Solution:
    def kthSmallestPath(self, destination, k):
        m = destination[1]
        n = destination[0] + destination[1]
        k -= 1

        @lru_cache(maxsize=None)
        def f(n, m):
            if n < m:
                return 0
            if n == 0 or m == 0:
                return 1

            return f(n - 1, m - 1) + f(n - 1, m)

        def solve(x, y, h):
            if x == 0:
                return ''

            t = f(x - 1, h - 1)
            if y >= t or h == 0:
                r = 'V' + solve(x - 1, y - t, h)
            else:
                r = 'H' + solve(x - 1, y, h - 1)
            return r

        return solve(n, k, m)


if __name__ == '__main__':
    print(Solution().kthSmallestPath([15, 15], 10))
    print(Solution().kthSmallestPath([15, 15], 300))
