from typing import List


class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = n >> 1
        ret = n * n
        yf = [[i, i] for i in range(m + 1)] + [[i, n - i - 1] for i in range(m)] + [[i, m] for i in range(m + 1, n)]
        print(yf)
        yy = [[False] * n for i in range(n)]
        for x, y in yf:
            yy[x][y] = True
        for i in range(3):
            for j in range(3):
                if i != j:
                    if i == 0 and j == 1:
                        x = x
                    t = 0
                    for r in range(n):
                        for c in range(n):
                            if yy[r][c]:
                                if grid[r][c] != i:
                                    t += 1
                            else:
                                if grid[r][c] != j:
                                    t += 1
                    ret = min(ret, t)
        return ret

if __name__ == '__main__':
    print(Solution().minimumOperationsToWriteY([[1,2,2],[1,1,0],[0,1,0]]))

