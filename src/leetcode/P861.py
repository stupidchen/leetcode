from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            if grid[i][0] == 0:
                for j in range(m):
                    grid[i][j] = 1 - grid[i][j]

        for j in range(1, m):
            o = 0
            for i in range(n):
                o += grid[i][j]
            if o < n - o:
                for i in range(n):
                    grid[i][j] = 1 - grid[i][j]

        r = 0
        for i in range(n):
            r += int(''.join(map(str, grid[i])), 2)
        return r


if __name__ == '__main__':
    print(Solution().matrixScore([[0, 1], [0, 1], [0, 1], [0, 0]]))
