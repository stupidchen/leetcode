class Solution:
    def maximalNetworkRank(self, n: int, roads):
        d = [[False] * n for i in range(n)]
        c = [0] * n
        for x, y in roads:
            d[x][y] = True
            d[y][x] = True
            c[x] += 1
            c[y] += 1

        r = 0
        for i in range(n):
            for j in range(i + 1, n):
                t = c[i] + c[j]
                if d[i][j]:
                    t -= 1
                r = max(r, t)
        return r


if __name__ == '__main__':
    print(Solution().maximalNetworkRank(n=4, roads=[[0, 1], [0, 3], [1, 2], [1, 3]]))
