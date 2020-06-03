from functools import lru_cache


class Solution:
    def twoCitySchedCost(self, costs):
        n = len(costs) >> 1

        @lru_cache(maxsize=None)
        def solve(i, j, k):
            if j == 0 and k == 0:
                return 0

            t = float('inf')
            if j > 0:
                t = min(t, solve(i - 1, j - 1, k) + costs[i][0])

            if k > 0:
                t = min(t, solve(i - 1, j, k - 1) + costs[i][1])
            return t

        return solve(len(costs) - 1, n, n)


if __name__ == '__main__':
    print(Solution().twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))
