from bisect import bisect
from random import random


class Solution:

    def __init__(self, w):
        s = sum(w)
        t = 0
        self.a = []
        for i in range(len(w)):
            t += w[i]
            self.a.append(t / s)

    def pickIndex(self):
        t = random()
        r = bisect(self.a, t)
        return r

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()