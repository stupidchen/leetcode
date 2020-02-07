DX = [0, 0, -1, 1]
DY = [-1, 1, 0, 0]

class Solution:
    def surfaceArea(self, grid):
        n = len(grid)
        if n == 0:
            return 0
        ret = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] != 0:
                    ret += 2
                for t in range(4):
                    tx = i + DX[t]
                    ty = j + DY[t]
                    if 0 <= tx < n and 0 <= ty < n:
                        if grid[i][j] > grid[tx][ty]:
                            ret += grid[i][j] - grid[tx][ty]
                    else:
                        ret += grid[i][j]
        return ret
