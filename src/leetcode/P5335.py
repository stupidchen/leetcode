DX = [-1, -1, 0, 0]
DY = [-1, 1, 1, -1]


def conflict(x1, y1, x2, y2):
    for i in range(4):
        if x1 + DX[i] == x2 and y1 + DY[i] == y2:
            return True
    return False


def find(e, q, c, x, t):
    q[x] = True
    for i in range(t):
        if not q[i] and e[x][i]:
            q[i] = True
            if i not in c or find(e, q, c, c[i], t) != 0:
                c[i] = x
                c[x] = i
                return 1
    return 0


class Solution:
    def maxStudents(self, seats):
        n = len(seats)
        m = len(seats[0])
        s = []
        for i in range(n):
            for j in range(m):
                if seats[i][j] != '#':
                    s.append((i, j))
        t = len(s)
        e = [[False] * t for i in range(t)]
        for i in range(t):
            for j in range(t):
                if i != j:
                    x1, y1 = s[i]
                    x2, y2 = s[j]
                    if conflict(x1, y1, x2, y2):
                        e[i][j] = True
                        e[j][i] = True

        c = {}
        r = 0
        for i in range(t):
            if i not in c:
                q = [False] * t
                r += find(e, q, c, i, t)
        return t - r


# For test only
SI = (([["#", ".", "#", "#", ".", "#"],
        [".", "#", "#", "#", "#", "."],
        ["#", ".", "#", "#", ".", "#"]],),
      ([[".", "#"],
        ["#", "#"],
        ["#", "."],
        ["#", "#"],
        [".", "#"]],),
      ([["#", ".", ".", ".", "#"],
        [".", "#", ".", "#", "."],
        [".", ".", "#", ".", "."],
        [".", "#", ".", "#", "."],
        ["#", ".", ".", ".", "#"]],))
SO = (4, 3, 10)
TM = 'maxStudents'
if __name__ == '__main__':
    from leetcode.PTester import PTester

    PTester(SI, SO, Solution, TM).run()
