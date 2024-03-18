import math
from collections import defaultdict, Counter


class Solution:
    def maximumLength(self, s: str) -> int:
        s = s + '#'
        n = len(s)
        counter = defaultdict(lambda: Counter())
        min_lengths = {}
        length = 1
        for i in range(1, n):
            if s[i] != s[i - 1]:
                for j in range(3):
                    if length > j:
                        counter[s[i - 1]][length - j] += j + 1
                min_length = max(length - 2, 1)
                min_lengths[s[i - 1]] = min(min_lengths.get(i, math.inf), min_length)
                length = 1
            else:
                length += 1

        res = -1
        for char, ct in counter.items():
            for length, freq in ct.items():
                if length >= min_lengths[char] and freq >= 3:
                    res = max(res, length)
        return res


