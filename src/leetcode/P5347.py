DX = [0, 0, 1, -1]
DY = [1, -1, 0, 0]


class Solution:
    def minCost(self, grid):
        n, m = len(grid), len(grid[0])
        f = [[-1] * m for i in range(n)]
        f[0][0] = 0
        q = [(0, 0)]
        h = 0
        while h < len(q):
            x, y = q[h]
            d = grid[x][y] - 1
            tx, ty = x + DX[d], y + DY[d]
            if 0 <= tx < n and 0 <= ty < m and (f[tx][ty] == -1 or f[tx][ty] > f[x][y]):
                f[tx][ty] = f[x][y]
                q.append((tx, ty))

            for i in range(4):
                if i != d:
                    tx, ty = x + DX[i], y + DY[i]
                    if 0 <= tx < n and 0 <= ty < m and (f[tx][ty] == -1 or f[tx][ty] > f[x][y] + 1):
                        f[tx][ty] = f[x][y] + 1
                        q.append((tx, ty))
            h += 1
        return f[n - 1][m - 1]


# For test only
SI = (([[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]],),)
SO = (3,)
TM = 'minCost'
if __name__ == '__main__':
    from leetcode.PTester import PTester

    PTester(SI, SO, Solution, TM).run()
