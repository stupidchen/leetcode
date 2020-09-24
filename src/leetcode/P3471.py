from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cs = Counter(s)
        ct = Counter(t)
        for c, i in ct.items():
            if cs[c] != i:
                return c
