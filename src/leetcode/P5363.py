class Solution:
    def maxSatisfaction(self, satisfaction):
        a = sorted(satisfaction)
        n = len(a)
        f = [[0] * n for i in range(n)]
        r = 0
        for i in range(n):
            f[i][0] = a[i]
            for j in range(1, i + 1):
                f[i][j] = f[i - 1][j - 1] + a[i] * (j + 1)
            r = max(r, max(f[i]))
        return r


if __name__ == '__main__':
    print(Solution().maxSatisfaction([-1, -4, -5]))
