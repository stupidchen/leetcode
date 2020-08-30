DX = (0, 0, 1, -1)
DY = (1, -1, 0, 0)


class Solution:
    def minDays(self, grid):
        n = len(grid)
        m = len(grid[0])

        def find(x, y, c, g, v):
            v[x][y] = c
            for i in range(4):
                tx, ty = x + DX[i], y + DY[i]
                if 0 <= tx < n and 0 <= ty < m and v[tx][ty] == 0 and g[tx][ty] != 0:
                    find(tx, ty, c, g, v)

        def count(g):
            t = 0
            v = [[0] * m for i in range(n)]
            for i in range(n):
                for j in range(m):
                    if v[i][j] == 0 and g[i][j] != 0:
                        t += 1
                        find(i, j, t, g, v)
            return t

        if count(grid) != 1:
            return 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count(grid) != 1:
                        return 1
                    grid[i][j] = 1

        return 2


if __name__ == '__main__':
    print(Solution().minDays([[0, 1, 0, 1, 1],
                              [1, 1, 1, 1, 1],
                              [1, 1, 1, 1, 1],
                              [1, 1, 1, 1, 0]]))
