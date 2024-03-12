from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        res = sum(nums[:3])
        for i in range(1, n):
            for j in range(i + 1, n):
                res = min(res, nums[i] + nums[j] + nums[0])
        return res

