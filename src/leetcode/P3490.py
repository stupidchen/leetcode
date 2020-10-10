class Solution:
    def findMinArrowShots(self, points):
        n = len(points)
        points = sorted(points)
        i = 0
        r = 0
        while i < n:
            r += 1
            j = i
            al, ar = points[i][0], points[i][1]
            while j < n and al <= points[j][0] <= ar:
                al = max(points[j][0], al)
                ar = min(points[j][1], ar)
                j += 1
            i = j
        return r
