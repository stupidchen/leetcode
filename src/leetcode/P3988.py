from collections import Counter
from typing import List


class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        board_t = map(list, zip(*board))
        row = list(Counter(tuple(row) for row in board).items())
        col = list(Counter(tuple(col) for col in board_t).items())
        if len(row) != 2 or len(col) != 2:
            return -1
        if abs(row[0][1] - row[1][1]) > 1 or abs(col[0][1] - col[1][1]) > 1:
            return -1
        p1 = ([0, 1] * ((n + 1) >> 1))[:n]
        p2 = ([1, 0] * ((n + 1) >> 1))[:n]
        r1 = sum(r != p for r, p in zip(row[0][0], p1))
        c1 = sum(c != p for c, p in zip(col[0][0], p1))
        r2 = sum(r != p for r, p in zip(row[0][0], p2))
        c2 = sum(c != p for c, p in zip(col[0][0], p2))

        r = [r for r in [r1, r2] if r & 1 == 0]
        c = [c for c in [c1, c2] if c & 1 == 0]
        return (min(r) >> 1) + (min(c) >> 1)
