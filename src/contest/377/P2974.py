from typing import List


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        for i in range(0, len(nums) >> 1):
            res.append(nums[(i << 1) + 1])
            res.append(nums[i << 1])
        return res

