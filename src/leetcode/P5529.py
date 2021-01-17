from functools import lru_cache

MAX_ROUND = 100
CATS_TURN = 0
MOUSES_TURN = 1

DX = [1, -1, 0, 0]
DY = [0, 0, 1, -1]
D = 4


class Solution:
    def canMouseWin(self, grid, catJump, mouseJump):
        n = len(grid)
        m = len(grid[0])
        mouseJump += 1
        catJump += 1
        food = None
        cat = None
        mouse = None
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'F':
                    food = (i, j)
                elif grid[i][j] == 'C':
                    cat = (i, j)
                elif grid[i][j] == 'M':
                    mouse = (i, j)

        @lru_cache(maxsize=None)
        def find(cx, cy, mx, my, t, r):
            if r == MAX_ROUND:
                return t == CATS_TURN

            if t == CATS_TURN:
                for d in range(D):
                    for k in range(catJump):
                        tx, ty = cx + k * DX[d], cy + k * DY[d]
                        if 0 <= tx < n and 0 <= ty < m:
                            if grid[tx][ty] != '#':
                                if (tx, ty) == food or (tx, ty) == (mx, my):
                                    return True
                                if not find(tx, ty, mx, my, MOUSES_TURN, r + 1):
                                    return True
                            else:
                                break
            else:
                for d in range(D):
                    for k in range(mouseJump):
                        tx, ty = mx + k * DX[d], my + k * DY[d]
                        if 0 <= tx < n and 0 <= ty < m:
                            if grid[tx][ty] != '#' and (tx, ty) != (cx, cy):
                                if (tx, ty) == food:
                                    return True
                                if not find(cx, cy, tx, ty, CATS_TURN, r + 1):
                                    return True
                            elif grid[tx][ty] == '#':
                                break

            return False

        return find(*cat, *mouse, MOUSES_TURN, 0)


if __name__ == '__main__':
    print(Solution().canMouseWin([".#M#.","##.##",".....","#C...","##.F."], 4, 2))
