from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        r = 0
        t = 0
        for i, v in enumerate(nums):
            if i == 0 or (v > nums[i - 1]):
                t += v
            else:
                r = max(t, r)
                t = v
        r = max(t, r)
        return r
