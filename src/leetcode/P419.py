DX = [1, 0, -1, 0]
DY = [0, 1, 0, -1]

class Solution:
    def countBattleships(self, board):
        n = len(board)
        if n == 0:
            return 0
        m = len(board[0])
        if m == 0:
            return 0

        ret = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'X':
                    c = 0
                    for k in range(4):
                        x, y = i + DX[k], j + DY[k]
                        if 0 <= x < n and 0 <= y < m and board[x][y] == 'X':
                            c += 1
                    if c == 0:
                        ret += 2
                    elif c == 1:
                        ret += 1
        ret >>= 1
        return ret

