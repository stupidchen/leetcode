class Solution:
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)
        f = [0] * (n + 1)
        for i in range(n):
            f[i + 1] = f[i] + cardPoints[i]

        t = n - k
        r = f[t]
        for i in range(1, n - t + 1):
            r = min(r, f[i + t] - f[i])
        return f[n] - r


if __name__ == '__main__':
    print(Solution().maxScore([1,79,80,1,1,1,200,1], 3))
    print(Solution().maxScore([1, 2, 3, 4, 5, 6, 1], 3))
