from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        n = len(groupSizes)
        r = []
        for i in range(1, max(groupSizes) + 1):
            g = []
            for j in range(n):
                if groupSizes[j] == i:
                    g.append(j)
                if len(g) == i:
                    r.append(g.copy())
                    g.clear()
        return r
