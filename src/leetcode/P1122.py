from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        o = {key: value for value, key in enumerate(arr2)}
        d = sorted([(o.get(key, len(arr1) + key), key) for value1, key in enumerate(arr1)])
        return list(map(lambda p: p[1], d))
