DX = [1, -1, 1, -1, 0, 0, 1, -1]
DY = [1, -1, -1, 1, 1, -1, 0, 0]


class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        m = len(grid[0])
        if grid[0][0] == 1:
            return -1

        q = [(0, 0)]
        v = {(0, 0): 1}
        h = 0
        while h < len(q):
            x, y = q[h]
            for i in range(8):
                tx, ty = x + DX[i], y + DY[i]
                if 0 <= tx < n and 0 <= ty < m and grid[tx][ty] == 0 and (tx, ty) not in v:
                    v[(tx, ty)] = v[(x, y)] + 1
                    q.append((tx, ty))
                    if (tx, ty) == (n - 1, m - 1):
                        return v[(tx, ty)]
            h += 1

        if (n - 1, m - 1) in v:
            return v[(n - 1, m - 1)]
        return -1


if __name__ == '__main__':
    print(Solution().shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]))
