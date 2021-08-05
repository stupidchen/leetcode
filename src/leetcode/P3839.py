class Solution:
    def stoneGame(self, piles):
        n = len(piles)
        if n == 0:
            return False
        if n == 1:
            return True
        s = [0] * (n + 1)
        for i in range(n):
            s[i + 1] = s[i] + piles[i]

        f = []
        for i in range(n):
            f.append([0] * n)
            f[i][i] = piles[i]

        for i in range(1, n):
            for j in range(n - i):
                l = j
                r = j + i
                f[l][r] = max(s[r + 1] - s[l + 1] - f[l + 1][r] + piles[l],
                              s[r] - s[l] - f[l][r - 1] + piles[r])

        return f[0][n - 1] > (s[n] >> 1)
