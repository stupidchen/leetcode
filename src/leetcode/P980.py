class Solution:
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        c = n * m
        sx, sy = 0, 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    sx, sy = i, j
                if grid[i][j] == -1:
                    c -= 1
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        v = [[False] * m for i in range(n)]
        ret = [0]

        def solve(x, y, w):
            if grid[x][y] == 2:
                if w == c:
                    ret[0] += 1
                return

            v[x][y] = True
            for i in range(4):
                tx, ty = x + dx[i], y + dy[i]
                if 0 <= tx < n and 0 <= ty < m:
                    if not v[tx][ty] and grid[tx][ty] != -1:
                        solve(tx, ty, w + 1)
            v[x][y] = False

        solve(sx, sy, 1)
        return ret[0]


if __name__ == '__main__':
    print(Solution().uniquePathsIII([[0,1],[2,0]]))
