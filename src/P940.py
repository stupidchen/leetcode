from functools import reduce

MODULO = 10 ** 9 + 7


class Solution:
    def distinctSubseqII(self, S):
        """
        :type S: str
        :rtype: int
        """
        n = len(S)
        f = [1] * n
        d = {S[0]: 1}
        for i in range(1, n):
            for k, v in d.items():
                if k != S[i]:
                    f[i] = (f[i] + v) % MODULO
            d[S[i]] = (d.setdefault(S[i], 0) + f[i]) % MODULO
        return reduce(lambda x, y: (x + y) % MODULO, f)


if __name__ == '__main__':
    print(Solution().distinctSubseqII('abc'))
