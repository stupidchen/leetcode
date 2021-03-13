MOD = 10 ** 9 + 7


class Solution:
    def numFactoredBinaryTrees(self, arr):
        arr = sorted(arr)
        n = len(arr)
        d = {}
        for i, v in enumerate(arr):
            d[v] = i
        f = [1] * n
        for i, v in enumerate(arr):
            for j in range(i):
                if v % arr[j] == 0 and v // arr[j] in d:
                    k = d[v // arr[j]]
                    f[i] = (f[i] + f[j] * f[k] % MOD) % MOD
        r = 0
        for v in f:
            r = (r + v) % MOD
        return r


if __name__ == '__main__':
    print(Solution().numFactoredBinaryTrees([2, 4]))
