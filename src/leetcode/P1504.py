import math


class Solution:
    def numSubmat(self, mat):
        n = len(mat)
        m = len(mat[0])
        v = [[0] * m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    v[i][j] = 1
                    if i > 0:
                        v[i][j] = v[i - 1][j] + 1

        r = 0
        for i in range(n):
            for j in range(m):
                w = math.inf
                for k in reversed(range(0, j + 1)):
                    w = min(v[i][k], w)
                    r += w
        return r


if __name__ == '__main__':
    print(Solution().numSubmat([[0, 1, 1, 0],
                                [0, 1, 1, 1],
                                [1, 1, 1, 0]]))
