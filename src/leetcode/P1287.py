from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr) >> 2
        c = 0
        l = 0
        for v in arr:
            if v != l:
                c = 1
            else:
                c += 1
            if c > n:
                return v
            l = v
