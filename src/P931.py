INF = 0xfffffff

class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        n = len(A)
        f = [[INF] * (n + 2) for i in range(n + 1)]
        f[0] = [0] * (n + 2)
        f[0][0] = INF
        f[0][n + 1] = INF
        for i in range(n):
            for j in range(n):
                f[i + 1][j + 1] = min(f[i][j], f[i][j + 1], f[i][j + 2]) + A[i][j]
        return min(f[n])

if __name__ == '__main__':
    print(Solution().minFallingPathSum([[3]]))