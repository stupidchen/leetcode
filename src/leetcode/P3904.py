from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        is_valid = lambda x: x != '.' and x.isdigit()

        grid = [0] * 9
        for i in range(n):
            row = 0
            column = 0
            for j in range(n):
                if is_valid(board[i][j]):
                    k = int(board[i][j])
                    if row | (1 << k) == row or k == 0:
                        return False
                    row = row | (1 << k)
                    gid = (i // 3) * 3 + (j // 3)
                    if grid[gid] | (1 << k) == grid[gid]:
                        return False
                    grid[gid] = grid[gid] | (1 << k)

                if is_valid(board[j][i]):
                    k = int(board[j][i])
                    if column | (1 << k) == column or k == 0:
                        return False
                    column = column | (1 << k)
        return True
