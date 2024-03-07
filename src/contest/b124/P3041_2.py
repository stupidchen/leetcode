from collections import defaultdict
from typing import List


class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        f = defaultdict(int)
        for num in nums:
            f[num + 1] = f[num] + 1
            f[num] = f[num - 1] + 1
        return max(f.values())
