DX = [0, 0, -1, 1]
DY = [1, -1, 0, 0]


class Solution:
    def orangesRotting(self, grid):
        n, m = len(grid), len(grid[0])
        f = []
        q = []
        for i in range(n):
            t = []
            for j in range(m):
                if grid[i][j] == 2:
                    t.append(0)
                    q.append((i, j))
                else:
                    t.append(-1)
            f.append(t)

        h = 0
        while h < len(q):
            x, y = q[h]
            for i in range(4):
                tx, ty = x + DX[i], y + DY[i]
                if 0 <= tx < n and 0 <= ty < m:
                    if grid[tx][ty] == 1 and f[tx][ty] == -1:
                        f[tx][ty] = f[x][y] + 1
                        q.append((tx, ty))
            h += 1

        r = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if f[i][j] == -1:
                        return -1
                    r = max(r, f[i][j])
        return r
