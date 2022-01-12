from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = -1
        n = len(arr)
        for i, v in enumerate(reversed(arr)):
            arr[n - i - 1] = m
            m = max(m, v)
        return arr
