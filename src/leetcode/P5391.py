MOD = 10 ** 9 + 7


class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        t = k + 1

        def init():
            return [[0] * t for i in range(m + 1)]

        f = [init() for i in range(n + 1)]
        d = [[0] * (m + 1) for i in range(t)]
        for i in range(m + 1):
            d[0][i] = 1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                for k in range(t):
                    f[i][j][k] = (f[i - 1][j][k] * j) % MOD
                    # if f[i][j][k] < 0:
                    #    f[i][j][k] += MOD

                    if k > 0:
                        f[i][j][k] = (f[i][j][k] + d[k - 1][j - 1]) % MOD
            d = [[0] * (m + 1) for q in range(t)]
            for k in range(t):
                for j in range(1, m + 1):
                    d[k][j] = d[k][j - 1] + f[i][j][k]

        r = 0
        for i in range(m + 1):
            r = (r + f[n][i][t - 1]) % MOD
        return r


if __name__ == '__main__':
    print(Solution().numOfArrays(9, 1, 1))
    print(Solution().numOfArrays(5, 2, 3))
    print(Solution().numOfArrays(37, 17, 7))
