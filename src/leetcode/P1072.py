from collections import defaultdict
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        c = defaultdict(lambda: 0)
        m = (1 << (len(matrix[0]))) - 1
        for i in matrix:
            v = 0
            for t in i:
                v = (v << 1) + t
            c[v] += 1
            c[m - v] += 1

        return max(c.values())


if __name__ == '__main__':
    print(Solution().maxEqualRowsAfterFlips([[0, 1], [1, 0]]))
