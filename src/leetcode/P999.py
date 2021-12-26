from typing import List

DI = [0, 0, 1, -1]
DJ = [1, -1, 0, 0]


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        n = len(board)
        r = 0
        for ri in range(n):
            for rj in range(n):
                if board[ri][rj] == 'R':
                    for d in range(4):
                        ti, tj = ri, rj
                        while 0 <= ti < n and 0 <= tj < n and board[ti][tj] != 'B':
                            if board[ti][tj] == 'p':
                                r += 1
                                break
                            ti, tj = ti + DI[d], tj + DJ[d]
        return r
