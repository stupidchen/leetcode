from math import inf


class Solution:
    def minCostConnectPoints(self, points) -> int:
        n = len(points)
        f = [[0] * n for i in range(n)]
        for i in range(n):
            for j in range(n):
                f[i][j] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        r = 0
        d = [f[0][i] for i in range(n)]
        v = [False] * n
        v[0] = True
        for i in range(n - 1):
            t, m = inf, -1
            for j in range(n):
                if not v[j] and d[j] < t:
                    t = d[j]
                    m = j
            v[m] = True
            r += t
            for j in range(n):
                if d[j] > f[m][j]:
                    d[j] = f[m][j]
        return r

