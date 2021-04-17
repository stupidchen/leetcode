from collections import defaultdict


class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])
        f = [[0] * m for i in range(n + 1)]
        for j in range(m):
            for i in range(n):
                f[i + 1][j] = f[i][j] + matrix[i][j]

        r = 0
        for r1 in range(n + 1):
            for r2 in range(r1 + 1, n + 1):
                d = defaultdict(lambda: 0)
                d[0] = 1
                t = 0
                for k in range(m):
                    t = f[r2][k] - f[r1][k] + t
                    r += d[t - target]
                    d[t] += 1
        return r


if __name__ == '__main__':
    print(Solution().numSubmatrixSumTarget(matrix=[[0, 1, 0], [1, 1, 1], [0, 1, 0]], target=0))
