from math import inf


class Solution:
    def minCostToMoveChips(self, position):
        r = inf
        for p in position:
            k = 0
            for q in position:
                t = abs(p - q)
                k += t & 1
            r = min(k, r)
        return r
