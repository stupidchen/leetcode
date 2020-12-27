class Solution:
    def findBall(self, grid):
        n = len(grid)
        m = len(grid[0])

        r = [-1] * m
        for i in range(m):
            c = i

            f = True
            for j in range(n):
                if grid[j][c] == 1:
                    if c + 1 < m and grid[j][c + 1] == 1:
                        c += 1
                    else:
                        f = False
                        break
                else:
                    if c > 0 and grid[j][c - 1] == -1:
                        c -= 1
                    else:
                        f = False
                        break
            if f:
                r[i] = c
        return r


if __name__ == '__main__':
    print(Solution().findBall([[1, -1, -1, 1, -1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1,
                                -1, 1, -1, -1, -1, -1, 1, -1, 1, 1, -1, -1, -1, -1, -1, 1],
                               [-1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, -1, -1, 1, 1, 1, 1, 1, 1, -1, 1,
                                -1, -1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 1, 1, -1, 1, 1],
                               [1, -1, -1, -1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, -1, 1, -1, 1,
                                -1, 1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, -1]]))
