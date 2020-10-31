class Solution:
    def maxWidthOfVerticalArea(self, points):
        n = len(points)
        points = sorted(points)
        r = 0
        for i in range(1, n):
            r = max(r, points[i][0] - points[i - 1][0])
        return r
