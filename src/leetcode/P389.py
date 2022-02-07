from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = Counter(s)
        d = Counter(t)
        for k, v in c.items():
            d[k] -= v
        for k, v in d.items():
            if v != 0:
                return k
