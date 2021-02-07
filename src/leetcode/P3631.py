from math import inf


class Solution:
    def shortestToChar(self, s: str, c: str):
        n = len(s)
        r = [inf] * n
        t = -1
        for i, v in enumerate(s):
            if v == c:
                t = i
            if t != -1:
                r[i] = min(r[i], i - t)
        t = -1
        for i, v in enumerate(reversed(s)):
            if v == c:
                t = i
            if t != -1:
                r[n - i - 1] = min(r[n - i - 1], i - t)
        return r
