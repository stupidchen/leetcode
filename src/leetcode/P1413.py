from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        s = 0
        r = 0
        for num in nums:
            s += num
            r = min(s, r)
        return max(0, 1 - r)
