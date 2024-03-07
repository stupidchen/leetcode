from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        s = nums[0] + nums[1]
        res = 1
        for i in range(1, n >> 1):
            if (i << 1) + 1 < n and nums[i << 1] + nums[(i << 1) + 1] == s:
                res += 1
            else:
                break
        return res
