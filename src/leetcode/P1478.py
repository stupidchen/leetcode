class Solution:
    def minDistance(self, houses, k):
        houses = sorted(houses)
        n = len(houses)

        f = []
        for i in range(n + 1):
            f.append([float('inf') / 2] * (k + 1))
        for i in range(k + 1):
            f[0][i] = 0

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                d = 0
                for t in reversed(range(i)):
                    d += houses[(t + i) >> 1] - houses[t]
                    f[i][j] = min(f[i][j], f[t][j - 1] + d)
        return f[n][k]


if __name__ == '__main__':
    print(Solution().minDistance(houses=[1, 4, 8, 10, 20], k=3))
