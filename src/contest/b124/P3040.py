from functools import lru_cache
from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(maxsize=n * n)
        def solve(left, right, target):
            if left >= right:
                return 0

            res = 0
            res = max(res, solve(left + 1, right - 1, target) + 1 if nums[left] + nums[right] == target else 0)
            res = max(res, solve(left + 2, right, target) + 1 if nums[left] + nums[left + 1] == target else 0)
            res = max(res, solve(left, right - 2, target) + 1 if nums[right - 1] + nums[right] == target else 0)
            return res

        return max(solve(1, n - 2, nums[0] + nums[n - 1]), solve(2, n - 1, nums[0] + nums[1]),
                   solve(0, n - 3, nums[n - 1] + nums[n - 2])) + 1


if __name__ == '__main__':
    r = Solution().maxOperations([3, 2, 1, 2, 3, 4])
    print(r)
