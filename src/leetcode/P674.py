from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        r = 1
        t = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                t += 1
            else:
                t = 1
            r = max(r, t)
        return r
