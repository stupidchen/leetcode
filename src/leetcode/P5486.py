from functools import lru_cache


class Solution:
    def minCost(self, n, cuts):
        @lru_cache(maxsize=None)
        def solve(l, r):
            if r - l <= 0:
                return 0
            if r - l == 1:
                return cuts[r] - cuts[l - 1]

            ret = float('inf')
            for i in range(l, r):
                ret = min(ret, solve(l, i) + solve(i + 1, r))
            return ret + cuts[r] - cuts[l - 1]

        cuts = [0] + sorted(cuts) + [n]
        return solve(1, len(cuts) - 1)


if __name__ == '__main__':
    print(Solution().minCost(n=7, cuts=[1, 3, 4, 5]))
    print(Solution().minCost(n = 9, cuts = [5,6,1,4,2]))
