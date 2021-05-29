class Solution:
    def getBiggestThree(self, grid):
        n, m = len(grid), len(grid[0])
        t = max(n, m)
        ds = [[0] for i in range(n + m)]
        rds = [[0] for i in range(n + m)]
        for i in range(n):
            for j in range(m):
                ds[i - j + m].append(ds[i - j + m][-1] + grid[i][j])
                rds[i + j].append(rds[i + j][-1] + grid[i][j])

        def check(x, y):
            return 0 <= x < n and 0 <= y < m

        def get_diag_sum(x, y, z):
            d = x - y + m
            if d < m:
                os = x
            else:
                os = y
            oe = os + z
            return ds[d][oe] - ds[d][os]

        def get_rdiag_sum(x, y, z):
            d = x + y
            if d > m - 1:
                os = m - 1 - y
            else:
                os = x
            oe = os + z
            return rds[d][oe] - rds[d][os]

        sums = set()
        for i in range(n):
            for j in range(m):
                sums.add(grid[i][j])
                for k in range(1, t):
                    if check(i - k, j) and check(i, j - k) and check(i + k, j) and check(i, j + k):
                        l = k + 1
                        s1 = get_diag_sum(i - k, j, l)
                        s2 = get_diag_sum(i, j - k, l)
                        s3 = get_rdiag_sum(i - k, j, l)
                        s4 = get_rdiag_sum(i, j + k, l)
                        s = s1 + s2 + s3 + s4 - grid[i - k][j] - grid[i][j - k] - grid[i + k][j] - grid[i][j + k]
                        sums.add(s)
                    else:
                        break
        sums = sorted(sums, reverse=True)
        return sums[:3]


if __name__ == '__main__':
    print(Solution().getBiggestThree(
        [[3, 4, 5, 1, 3], [3, 3, 4, 2, 3], [20, 30, 200, 40, 10], [1, 5, 5, 4, 1], [4, 3, 2, 2, 5]]))
