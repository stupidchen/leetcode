class Solution:
    def cherryPickup(self, grid):
        n = len(grid)
        m = len(grid[0])

        def init():
            return [[None] * m for i in range(m)]

        f = [init() for i in range(2)]
        f[0][0][m - 1] = grid[0][0] + grid[0][m - 1]
        r = 0
        for i in range(1, n):
            c = i & 1
            d = 1 - c
            for j in range(m):
                for k in range(m):
                    t = float('-inf')
                    for dj in range(3):
                        for dk in range(3):
                            lj = j + dj - 1
                            lk = k + dk - 1
                            if 0 <= lj < m and 0 <= lk < m and f[d][lj][lk] is not None:
                                t = max(t, f[d][lj][lk] + grid[i][j] + grid[i][k] - (0 if j != k else grid[i][j]))
                    if t < 0:
                        t = None
                    f[c][j][k] = t
                    if t is not None:
                        r = max(t, r)
        return r
