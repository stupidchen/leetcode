DX = [1, -1, 0, 0]
DY = [0, 0, 1, -1]


class Solution:
    @staticmethod
    def flood(map, q):
        n = len(map)
        m = len(map[0])
        h = -1
        r = [[False] * m for i in range(n)]
        for c in q:
            x, y = c
            r[x][y] = True
        while h + 1 < len(q):
            h += 1
            x, y = q[h]
            for i in range(4):
                tx, ty = x + DX[i], y + DY[i]
                if 0 <= tx < n and 0 <= ty < m and map[tx][ty] >= map[x][y] and not r[tx][ty]:
                    r[tx][ty] = True
                    q.append((tx, ty))
        return r

    def pacificAtlantic(self, matrix):
        n = len(matrix)
        if n == 0:
            return []
        m = len(matrix[0])
        aq, pq = [], []
        for i in range(n):
            aq.append((i, 0))
            pq.append((i, m - 1))
        for i in range(m):
            aq.append((0, i))
            pq.append((n - 1, i))
        ra, rp = Solution.flood(matrix, aq), Solution.flood(matrix, pq)
        r = []
        for i in range(n):
            for j in range(m):
                if ra[i][j] and rp[i][j]:
                    r.append([i, j])
        return r
