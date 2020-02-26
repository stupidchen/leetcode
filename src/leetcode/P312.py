from functools import lru_cache


class Solution:
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        n = len(nums)

        @lru_cache(maxsize=None)
        def solve(l, r):
            if l > r:
                return 0

            ret = 0
            for i in range(l, r + 1):
                t = solve(l, i - 1) + solve(i + 1, r)
                ret = max(ret, nums[i] * nums[l - 1] * nums[r + 1] + t)
            return ret

        return solve(1, n - 2)


# For test only
SI = (([3, 1, 5, 8],),)
SO = (167,)
TM = 'maxCoins'
if __name__ == '__main__':
    from leetcode.PTester import PTester

    PTester(SI, SO, Solution, TM).run()
