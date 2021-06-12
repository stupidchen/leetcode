class Solution:
    def largestMagicSquare(self, grid) -> int:
        n, m = len(grid), len(grid[0])
        ds = [[0] for i in range(n + m)]
        rds = [[0] for i in range(n + m)]
        rs, cs = [[0] * (m + 1) for i in range(n)], [[0] * (n + 1) for i in range(m)]
        for i in range(n):
            for j in range(m):
                rs[i][j + 1] = rs[i][j] + grid[i][j]
                cs[j][i + 1] = cs[j][i] + grid[i][j]
                ds[i - j + m].append(ds[i - j + m][-1] + grid[i][j])
                rds[i + j].append(rds[i + j][-1] + grid[i][j])

        def get_row_sum(x, y, z):
            return rs[z][y + 1] - rs[z][x]

        def get_column_sum(x, y, z):
            return cs[z][y + 1] - cs[z][x]

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

        for k in reversed(range(1, min(n, m) + 1)):
            for i in range(n - k + 1):
                for j in range(m - k + 1):
                    f = True
                    m_ds = get_diag_sum(i, j, k)
                    m_rds = get_rdiag_sum(i, j + k - 1, k)
                    s = get_row_sum(j, j + k - 1, i)
                    if s == m_ds == m_rds:
                        for t in range(i + 1, i + k):
                            if get_row_sum(j, j + k - 1, t) != s:
                                f = False
                                break
                        if not f:
                            continue
                        for t in range(j, j + k):
                            if get_column_sum(i, i + k - 1, t) != s:
                                f = False
                                break
                        if f:
                            return k


if __name__ == '__main__':
    print(Solution().largestMagicSquare([[2, 1], [2, 2]]))
