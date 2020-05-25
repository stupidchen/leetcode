class Solution:
    def maxUncrossedLines(self, A, B):
        n = len(A)
        m = len(B)
        f = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(n):
            for j in range(m):
                f[i + 1][j + 1] = max(f[i][j + 1], f[i + 1][j])
                if A[i] == B[j]:
                    f[i + 1][j + 1] = max(f[i + 1][j + 1], f[i][j] + 1)
        return f[n][m]


if __name__ == '__main__':
    print(Solution().maxUncrossedLines(A=[2, 5, 1, 2, 5], B=[10, 5, 2, 1, 5, 2]))
