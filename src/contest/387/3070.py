from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        p = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(n):
            for j in range(m):
                p[i + 1][j + 1] = p[i][j + 1] + p[i + 1][j] - p[i][j] + grid[i][j]
        r = 0
        for i in range(n):
            for j in range(m):
                if p[i + 1][j + 1] <= k:
                    r += 1
        return r


if __name__ == '__main__':
    print(Solution().countSubmatrices([[1, 10], [7, 2], [9, 1], [4, 1]], 8))
