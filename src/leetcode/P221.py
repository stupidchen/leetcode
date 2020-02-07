class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        if m == 0:
            return 0
        f = [0] * (m + 1)
        p = 0
        ret = 0
        for i in range(n):
            for j in range(m):
                p, f[j + 1] = f[j + 1], min(f[j], f[j + 1], p) + 1 if matrix[i][j] == '1' else 0
                ret = max(ret, f[j + 1])
        return ret * ret
