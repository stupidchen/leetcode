class Solution:
    def countKeyChanges(self, s: str) -> int:
        res = 0
        for lc, c in zip(s.upper()[:-1], s.upper()[1:]):
            if lc != c:
                res += 1
        return res

