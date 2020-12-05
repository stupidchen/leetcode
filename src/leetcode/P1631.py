from math import inf

DX = [0, 0, 1, -1]
DY = [1, -1, 0, 0]


class Solution:
    def minimumEffortPath(self, heights):
        q = [(0, 0)]
        n = len(heights)
        m = len(heights[0])
        f = [[inf] * m for i in range(n)]
        f[0][0] = 0
        h = 0
        while h < len(q):
            x, y = q[h]

            for i in range(4):
                tx, ty = x + DX[i], y + DY[i]
                if 0 <= tx < n and 0 <= ty < m:
                    d = max(f[x][y], abs(heights[tx][ty] - heights[x][y]))
                    if d < f[tx][ty]:
                        f[tx][ty] = d
                        q.append((tx, ty))
            h += 1

        return f[n - 1][m - 1]
