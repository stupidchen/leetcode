from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        r = 0
        n = len(mat)
        for i in range(n):
            t = n - i - 1
            r += mat[i][i]
            if t != i:
                r += mat[i][t]
        return r
