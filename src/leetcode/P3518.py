class Solution:
    def maxPower(self, s: str) -> int:
        r = 0
        t = 0
        l = None
        for c in s:
            if c != l:
                t = 1
            else:
                t += 1
            r = max(r, t)
            l = c
        return r
