class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        rs = ''.join(reversed(s))
        n = len(s)
        f = [[0] * (n + 1) for i in range(n + 1)]

        for i in range(n):
            for j in range(n):
                f[i + 1][j + 1] = max(f[i][j + 1], f[i + 1][j])
                if s[i] == rs[j]:
                    f[i + 1][j + 1] = f[i][j] + 1

        return f[n][n]


if __name__ == '__main__':
    print(Solution().longestPalindromeSubseq('bbbab'))
