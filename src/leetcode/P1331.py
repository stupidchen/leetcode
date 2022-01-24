from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        p = sorted(arr)
        d = {}
        last = None
        r = 0
        for a in p:
            if last != a:
                r += 1
            d[a] = r
            last = a
        ret = []
        for a in arr:
            ret.append(d[a])
        return ret
