class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        n, m = len(text1), len(text2)
        f = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(n):
            for j in range(m):
                f[i + 1][j + 1] = max(f[i + 1][j], f[i][j + 1])
                if text1[i] == text2[j]:
                    f[i + 1][j + 1] = max(f[i][j] + 1, f[i + 1][j + 1])
        return f[n][m]
