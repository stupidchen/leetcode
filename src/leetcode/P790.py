MOD = 10 ** 9 + 7


class Solution:
    def numTilings(self, n: int) -> int:
        if n <= 3:
            if n == 1:
                return 1
            elif n == 2:
                return 2
            else:
                return 5
        f = [0] * (n + 1)
        f[1] = 1
        f[2] = 2
        f[3] = 5
        for i in range(4, n + 1):
            f[i] = ((f[i - 1] << 1) + f[i - 3]) % MOD
        return f[n]
