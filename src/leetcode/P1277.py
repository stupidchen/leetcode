class Solution:
    def countSquares(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        f = [[0] * m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    f[i][j] = 0
                else:
                    f[i][j] = min(f[i - 1][j - 1], min(f[i - 1][j] if i > 0 else 0, f[i][j - 1] if j > 0 else 0)) + 1

        r = sum(sum(f[i]) for i in range(n))

        return r


if __name__ == '__main__':
    print(Solution().countSquares([
            [1, 0, 1, 0, 1],
            [1, 0, 0, 1, 1],
            [0, 1, 0, 1, 1],
            [1, 0, 0, 1, 1]
    ]))
