DX = [0, 1, 0, -1]
DY = [1, 0, -1, 0]


def valid(l, c, lx, ly, cx, cy):
    if l == 1:
        if c != 2:
            if (c == 3 or c == 5 or c == 1) and ly < cy:
                return True
            if (c == 4 or c == 6 or c == 1) and ly > cy:
                return True
        return False

    if l == 2:
        if c != 1:
            if (c == 3 or c == 4 or c == 2) and lx > cx:
                return True
            if (c == 5 or c == 6 or c == 2) and lx < cx:
                return True
        return False

    if l == 3:
        if lx < cx:
            if c == 2 or c == 5 or c == 6:
                return True
            return False
        if ly > cy:
            if c == 1 or c == 4 or c == 6:
                return True
            return False

    if l == 4:
        if lx < cx:
            if c == 2 or c == 5 or c == 6:
                return True
            return False
        if ly < cy:
            if c == 1 or c == 3 or c == 5:
                return True
            return False

    if l == 5:
        if lx > cx:
            if c == 2 or c == 3 or c == 4:
                return True
            return False
        if ly > cy:
            if c == 1 or c == 4 or c == 6:
                return True
            return False

    if l == 6:
        if lx > cx:
            if c == 2 or c == 3 or c == 4:
                return True
            return False
        if ly < cy:
            if c == 1 or c == 3 or c == 5:
                return True
            return False

    return False


class Solution:
    def hasValidPath(self, grid):
        n, m = len(grid), len(grid[0])
        if n == 1 and m == 1:
            return True
        f = [[False] * m for i in range(n)]
        f[0][0] = True
        q = [(0, 0)]
        h = 0
        while h < len(q):
            x, y = q[h]
            for i in range(4):
                tx, ty = x + DX[i], y + DY[i]
                if 0 <= tx < n and 0 <= ty < m and not f[tx][ty] and valid(grid[x][y], grid[tx][ty], x, y, tx, ty):
                    q.append((tx, ty))
                    f[tx][ty] = True
            h += 1
        return f[n - 1][m - 1]


if __name__ == '__main__':
    print(Solution().hasValidPath([[1,2,1],[1,2,1]]))
    print(Solution().hasValidPath([[1,1,1,1,1,1,3]]))
