DX = [0, 0, 1, -1]
DY = [1, -1, 0, 0]


class Solution:
    def nearestExit(self, maze, entrance):
        n = len(maze)
        m = len(maze[0])
        entrance = tuple(entrance)
        q = [entrance]
        steps = {entrance: 0}
        h = 0
        while h < len(q):
            x, y = q[h]
            for i in range(4):
                tx, ty = x + DX[i], y + DY[i]
                if 0 <= tx < n and 0 <= ty < m:
                    if maze[tx][ty] == '.' and (tx, ty) not in steps:
                        q.append((tx, ty))
                        steps[(tx, ty)] = steps[(x, y)] + 1
                elif (x, y) != entrance:
                    return steps[(x, y)]

            h += 1

        return -1
