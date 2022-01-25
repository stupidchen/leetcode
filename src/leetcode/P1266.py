from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        ret = 0
        for i in range(1, n):
            ret += max(abs(points[i - 1][0] - points[i][0]), abs(points[i - 1][1] - points[i][1]))
        return ret
