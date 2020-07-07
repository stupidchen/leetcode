class Solution:
    def islandPerimeter(self, grid):
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])

        def d():
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            i = 0
            while i < 4:
                yield dx[i], dy[i]
                i += 1

        r = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dg = d()
                    while 1:
                        try:
                            dx, dy = next(dg)
                            tx, ty = i + dx, j + dy
                            if 0 <= tx < n and 0 <= ty < m:
                                r += 1 - grid[tx][ty]
                            else:
                                r += 1
                        except StopIteration:
                            break
        return r


if __name__ == '__main__':
    print(Solution().islandPerimeter([[0, 1, 0, 0],
                                      [1, 1, 1, 0],
                                      [0, 1, 0, 0],
                                      [1, 1, 0, 0]]))
