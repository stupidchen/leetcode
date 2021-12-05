from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        l = []
        n = len(arr)
        for a in arr:
            if a != 0:
                l.append(a)
            else:
                l.append(0)
                l.append(0)
            if len(l) >= n:
                break
        for i in range(n):
            arr[i] = l[i]

