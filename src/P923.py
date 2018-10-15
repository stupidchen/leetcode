MAXA = 300
MODULO = 10 ** 9 + 7

class Solution:
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        n = len(A)
        f = []
        for i in range(n + 1):
            f.append([0] * (MAXA + 1))
        for i in reversed(range(n)):
            for j in range(MAXA + 1):
                f[i][j] = f[i + 1][j]
            f[i][A[i]] += 1
        ret = 0
        d = [0] * (MAXA + 1)
        d[A[0]] += 1
        for i in range(1, n - 1):
            t = target - A[i]
            for j in range(t + 1):
                ret = (ret + d[t - j] * f[i + 1][j]) % MODULO
            d[A[i]] += 1
        return ret
