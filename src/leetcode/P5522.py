from math import inf


class Solution:
    def connectTwoGroups(self, cost):
        n = len(cost)
        m = len(cost[0])
        b = 1 << m
        f = [[inf] * b for i in range(n + 1)]
        f[0][0] = 0

        for i in range(n):
            for j in range(b):
                for k in range(m):
                    f[i + 1][j] = min(f[i + 1][j], f[i][j] + cost[i][k])
                    if j | (1 << k) <= j:
                        f[i + 1][j] = min(f[i + 1][j], f[i][j - (1 << k)] + cost[i][k])
                        f[i + 1][j] = min(f[i + 1][j], f[i + 1][j - (1 << k)] + cost[i][k])

        return f[n][b - 1]


if __name__ == '__main__':
    print(Solution().connectTwoGroups(cost=[[1, 3, 5], [4, 1, 1], [1, 5, 3]]))
    print(Solution().connectTwoGroups(cost=[[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]))
    print(Solution().connectTwoGroups(cost=[[15, 96], [36, 2]]))
