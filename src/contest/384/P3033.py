from copy import deepcopy
from typing import List


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        res = deepcopy(matrix)
        max_num = [max([matrix[i][j] for i in range(n)]) for j in range(m)]
        for i in range(n):
            for j in range(m):
                if res[i][j] == -1:
                    res[i][j] = max_num[j]
        return res


if __name__ == '__main__':
    r = Solution().modifiedMatrix([[1, 2, -1], [4, -1, 6], [7, 8, 9]])
    print(r)
