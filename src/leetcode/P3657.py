from collections import Counter


class Solution:
    def distributeCandies(self, candyType):
        c = Counter(candyType)
        n = len(candyType)
        m = n >> 1
        if m > len(c):
            return len(c)
        else:
            return m
