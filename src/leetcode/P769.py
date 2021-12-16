from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        m = -1
        r = 0
        for i, v in enumerate(arr):
            m = max(v, m)
            if i == m:
                r += 1
        return r
