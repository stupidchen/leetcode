from typing import List

WINNER = ['Draw', 'A', 'B']


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        s = [[0] * 3 for i in range(3)]
        t = 1
        for x, y in moves:
            s[x][y] = t
            t = 3 - t

        if s[0][0] == s[0][1] == s[0][2] != 0:
            return WINNER[s[0][0]]
        if s[1][0] == s[1][1] == s[1][2] != 0:
            return WINNER[s[1][0]]
        if s[2][0] == s[2][1] == s[2][2] != 0:
            return WINNER[s[2][0]]

        if s[0][0] == s[1][0] == s[2][0] != 0:
            return WINNER[s[0][0]]
        if s[0][1] == s[1][1] == s[2][1] != 0:
            return WINNER[s[0][1]]
        if s[0][2] == s[1][2] == s[2][2] != 0:
            return WINNER[s[0][2]]

        if s[0][0] == s[1][1] == s[2][2] != 0:
            return WINNER[s[0][0]]

        if s[0][2] == s[1][1] == s[2][0] != 0:
            return WINNER[s[0][2]]

        if len(moves) == 9:
            return WINNER[0]
        return 'Pending'
