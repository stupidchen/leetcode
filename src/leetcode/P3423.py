from collections import defaultdict
from functools import reduce


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = defaultdict(lambda: 0)
        for l in s:
            d[l] += 1
        return (sum([v >> 1 for v in d.values()]) << 1) + reduce(lambda x, y: x | y, [v & 1 for v in d.values()], 0)
