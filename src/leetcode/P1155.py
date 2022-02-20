MOD = 10 ** 9 + 7


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        f = {(0, i + 1): 1 for i in range(k)}
        for i in range(1, n):
            for j in range(1, target + 1):
                it = (i, j)
                f[it] = 0
                for t in range(k):
                    tt = (i - 1, j - t - 1)
                    if tt in f:
                        f[it] = (f[it] + f[tt]) % MOD
        return f.get((n - 1, target), 0)


if __name__ == '__main__':
    print(Solution().numRollsToTarget(n=1, k=2, target=3))
