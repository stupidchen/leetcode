MOD = 10 ** 9 + 7


class Solution:
    def maxProductPath(self, grid):
        n = len(grid)
        m = len(grid[0])
        fp = [[None] * m for i in range(n)]
        fn = [[None] * m for i in range(n)]

        def tmax(x, y):
            if x is None:
                return y
            if y is None:
                return x
            return max(x, y)

        def tmin(x, y):
            if x is None:
                return y
            if y is None:
                return x
            return min(x, y)

        if grid[0][0] == 0:
            fn[0][0] = fp[0][0] = 0
        else:
            if grid[0][0] > 0:
                fp[0][0] = grid[0][0]
            else:
                fn[0][0] = grid[0][0]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                if grid[i][j] != 0:
                    if i > 0:
                        if fp[i - 1][j] is not None:
                            fp[i][j] = tmax(fp[i][j], fp[i - 1][j] * grid[i][j])
                            fn[i][j] = tmin(fn[i][j], fp[i - 1][j] * grid[i][j])
                        if fn[i - 1][j] is not None:
                            fn[i][j] = tmin(fn[i][j], fn[i - 1][j] * grid[i][j])
                            fp[i][j] = tmax(fp[i][j], fn[i - 1][j] * grid[i][j])

                    if j > 0:
                        if fp[i][j - 1] is not None:
                            fp[i][j] = tmax(fp[i][j], fp[i][j - 1] * grid[i][j])
                            fn[i][j] = tmin(fn[i][j], fp[i][j - 1] * grid[i][j])

                        if fn[i][j - 1] is not None:
                            fp[i][j] = tmax(fp[i][j], fn[i][j - 1] * grid[i][j])
                            fn[i][j] = tmin(fn[i][j], fn[i][j - 1] * grid[i][j])
                else:
                    c = False
                    if i > 0:
                        if fp[i - 1][j] is not None or fn[i - 1][j] is not None:
                            c = True
                    if j > 0:
                        if fp[i][j - 1] is not None or fn[i][j - 1] is not None:
                            c = True
                    if c:
                        fp[i][j] = 0
                        fn[i][j] = 0
        if fp[n - 1][m - 1] < 0:
            return -1
        return fp[n - 1][m - 1] % MOD


if __name__ == '__main__':
    print(Solution().maxProductPath(grid=[[-1, -2, -3],
                                          [-2, -3, -3],
                                          [-3, -3, -2]]))
