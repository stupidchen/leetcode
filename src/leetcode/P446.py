from collections import Counter
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        f = [Counter() for i in range(n)]
        ret = 0
        for i in range(n):
            for j in range(i):
                d = nums[i] - nums[j]
                f[i][d] += f[j][d] + 1

            ret += sum(f[i].values())
        ret -= n * (n - 1) >> 1
        return ret
