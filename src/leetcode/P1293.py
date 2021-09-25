from typing import List

DX = [1, -1, 0, 0]
DY = [0, 0, 1, -1]


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        if n * m == 1:
            return 0
        g = [[set() for j in range(m)] for i in range(n)]
        g[0][0].add(0)
        q = [(0, 0, 0, 0)]
        h = 0
        while h < len(q):
            x, y, o, s = q[h]
            ts = s + 1
            for i in range(4):
                tx = x + DX[i]
                ty = y + DY[i]
                if (0 <= tx < n) and (0 <= ty < m):
                    to = o + grid[tx][ty]
                    if tx == n - 1 and ty == m - 1:
                        return ts
                    if to <= k and to not in g[tx][ty]:
                        g[tx][ty].add(to)
                        q.append((tx, ty, to, ts))
            h += 1
        return -1


if __name__ == '__main__':
    print(Solution().shortestPath(grid=
                                  [[0, 0, 0],
                                   [1, 1, 0],
                                   [0, 0, 0],
                                   [0, 1, 1],
                                   [0, 0, 0]],
                                  k=1))
