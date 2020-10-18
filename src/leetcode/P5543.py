from collections import defaultdict
from math import inf


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        min_c = defaultdict(lambda: inf)
        max_c = defaultdict(lambda: -inf)
        for i in range(len(s)):
            c = s[i]
            min_c[c] = min(min_c[c], i)
            max_c[c] = max(max_c[c], i)

        r = -1
        for c in min_c.keys():
            r = max(r, max_c[c] - min_c[c] - 1)
        return r
