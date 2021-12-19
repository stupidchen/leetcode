from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        arr.sort()
        diff = [arr[i] - arr[i - 1] for i in range(1, n)]
        min_diff = min(diff)
        r = []
        for i in range(1, n):
            if arr[i] - arr[i - 1] == min_diff:
                r.append([arr[i - 1], arr[i]])
        return r
