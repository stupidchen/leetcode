MOD = 10 ** 9 + 7


class Solution:
    def numberWays(self, hats):
        n = len(hats)
        m = 1 << n
        f = [[0] * m for i in range(41)]
        f[0][0] = 1
        h = [[]]
        for i in range(1, 41):
            h.append([])
            for j in range(n):
                if i in hats[j]:
                    h[i].append(j)
        for i in range(1, 41):
            for j in range(1, m):
                for k in h[i]:
                    if j ^ (1 << k) < j:
                        f[i][j] = (f[i][j] + f[i - 1][j - (1 << k)]) % MOD
            for j in range(m):
                f[i][j] = (f[i - 1][j] + f[i][j]) % MOD
        return f[40][m - 1]


if __name__ == '__main__':
    print(Solution().numberWays([[1,2,3],[2,3,5,6],[1,3,7,9],[1,8,9],[2,5,7]]))
    print(Solution().numberWays([[3, 5, 1], [3, 5]]))
    print(Solution().numberWays([[i for i in range(1, 41)] for i in range(10)]))
