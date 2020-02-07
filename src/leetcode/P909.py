class Solution:
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        m = len(board[0])
        t = 1
        s = {}
        v = []
        for i in reversed(range(n)):
            y = range(m)
            v.append([-1] * m)
            if ((n - i) & 1) == 0:
                y = reversed(y)
            for j in y:
                s[t] = (i, j)
                t += 1

        h = 0
        ta = 1
        q = [1]
        v[n - 1][0] = 0
        e = n * m
        while h < ta:
            if q[h] == e:
                break
            x = s[q[h]][0]
            y = s[q[h]][1]
            for i in range(6):
                t = q[h] + i + 1
                if t <= e:
                    tx = s[t][0]
                    ty = s[t][1]
                    if board[tx][ty] != -1:
                        t = board[tx][ty]
                        tx = s[t][0]
                        ty = s[t][1]
                        if v[tx][ty] == -1 or v[tx][ty] > v[x][y] + 1:
                            v[tx][ty] = v[x][y] + 1
                            q.append(t)
                            ta += 1
                    else:
                        if v[tx][ty] == -1 or v[tx][ty] > v[x][y] + 1:
                            v[tx][ty] = v[x][y] + 1
                            q.append(t)
                            ta += 1
            h += 1

        return v[s[e][0]][s[e][1]]


if __name__ == '__main__':
    print(Solution().snakesAndLadders([
        [-1, -1, -1, -1, -1, -1]]
        ))
