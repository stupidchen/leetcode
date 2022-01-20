from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        s = sorted(heights)
        r = 0
        for x, y in zip(s, heights):
            if x != y:
                r += 1
        return r
