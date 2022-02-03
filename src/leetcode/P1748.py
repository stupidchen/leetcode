from collections import Counter
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        c = Counter(nums)
        r = 0
        for k, v in c.items():
            if v == 1:
                r += k
        return r
