class Solution:
    def minCost(self, houses, cost, m, n, target):
        def init(first=False):
            if first:
                return [([0] + [-1] * target) for i in range(n)]
            else:
                return [[-1] * (target + 1) for i in range(n)]

        f = [init(), init(True)]
        for i in range(m):
            c = i & 1
            d = 1 - c
            f[c] = init()
            if houses[i] == 0:
                for j in range(n):
                    for k in range(1, min(i + 1, target) + 1):
                        f[c][j][k] = -1
                        if f[d][j][k] != -1:
                            f[c][j][k] = f[d][j][k] + cost[i][j]
                        for l in range(n):
                            if l != j and f[d][l][k - 1] != -1:
                                f[c][j][k] = f[d][l][k - 1] + cost[i][j] \
                                    if f[c][j][k] == -1 or f[c][j][k] > f[d][l][k - 1] + cost[i][j] else f[c][j][k]
            else:
                j = houses[i] - 1
                for k in range(1, min(i + 1, target) + 1):
                    f[c][j][k] = -1
                    if f[d][j][k] != -1:
                        f[c][j][k] = f[d][j][k]
                    for l in range(n):
                        if l != j and f[d][l][k - 1] != -1:
                            f[c][j][k] = f[d][l][k - 1] \
                                if f[c][j][k] == -1 or f[c][j][k] > f[d][l][k - 1] else f[c][j][k]
        r = -1
        c = (m - 1) & 1
        for i in range(n):
            if f[c][i][target] != -1:
                r = f[c][i][target] if r == -1 or r > f[c][i][target] else r
        return r


if __name__ == '__main__':
    print(Solution().minCost(houses=[0, 2, 1, 2, 0], cost=[[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]], m=5, n=2,
                             target=3))
