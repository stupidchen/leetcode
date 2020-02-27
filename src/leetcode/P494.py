from functools import lru_cache


class Solution:
    def findTargetSumWays(self, nums, S):
        n = len(nums)

        @lru_cache(maxsize=None)
        def solve(s, m):
            if m >= n:
                if s == 0:
                    return 1
                return 0

            return solve(s + nums[m], m + 1) + solve(s - nums[m], m + 1)

        return solve(S, 0)


# For test only
SI = (([1, 1, 1, 1, 1], 3,),)
SO = (5,)
TM = 'findTargetSumWays'
if __name__ == '__main__':
    from leetcode.PTester import PTester

    PTester(SI, SO, Solution, TM).run()
