from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diagonal = max(map(lambda x: x[0] ** 2 + x[1] ** 2, dimensions))
        res = 0
        for dimension in dimensions:
            if dimension[0] ** 2 + dimension[1] ** 2 == max_diagonal:
                res = max(res, dimension[0] * dimension[1])
        return res

