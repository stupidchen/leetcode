from collections import Counter
from typing import List


class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        c = Counter()
        for num in nums:
            c[num & 1] += 1

        return c[0] > 1

