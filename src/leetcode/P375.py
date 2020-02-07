from functools import lru_cache


class Solution:
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """

        @lru_cache(maxsize=None)
        def solve(l, r):
            if l >= r:
                return 0

            ret = n * n
            for i in range(l, r + 1):
                ret = min(ret, i + max(solve(l, i - 1), solve(i + 1, r)))
            return ret

        return solve(1, n)


if __name__ == '__main__':
    print(Solution().getMoneyAmount(10))
