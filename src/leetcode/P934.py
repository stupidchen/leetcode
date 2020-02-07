dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def abs(x):
    if x < 0:
        x = -x
    return x


class Solution:
    def color(self, a, b, c, n, m, s):
        q = [s]
        h = 0
        t = 0
        b[s[0]][s[1]] = c
        while h <= t:
            for i in range(4):
                tx = q[h][0] + dx[i]
                ty = q[h][1] + dy[i]
                if 0 <= tx < n and 0 <= ty < m:
                    if a[tx][ty] == 1 and b[tx][ty] != c:
                        b[tx][ty] = c
                        t += 1
                        q.append((tx, ty))
            h += 1

    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        n = len(A)
        m = len(A[0])
        board = []
        for i in range(n):
            board.append([0] * m)
        color = 1
        for i in range(n):
            for j in range(m):
                if A[i][j] == 1 and board[i][j] == 0:
                    self.color(A, board, color, n, m, (i, j))
                    color += 1
        edge = [[], []]
        for i in range(n):
            for j in range(m):
                if A[i][j] != 0:
                    is_edge = False
                    for k in range(4):
                        ti = i + dx[k]
                        tj = j + dy[k]
                        if 0 <= ti < n and 0 <= tj < m and A[ti][tj] == 0:
                            is_edge = True
                            break
                    if is_edge:
                        edge[board[i][j] - 1].append((i, j))
        ret = 0xffffffff
        for i in edge[0]:
            for j in edge[1]:
                t = abs(i[0] - j[0]) + abs(i[1] - j[1]) - 1
                ret = min(t, ret)
        return ret


if __name__ == '__main__':
    print(Solution().shortestBridge(
        [[0, 1, 0], [0, 0, 0], [0, 0, 1]]))
