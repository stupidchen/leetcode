MODULO = 10 ** 9 + 7

class Solution:
    def sumSubseqWidths(self, A):
        a = sorted(A)
        s0 = 0
        s1 = 0
        n = len(a)
        for i in reversed(range(1, n)):
            s0 = 2 * (s0 + a[i]) % MODULO

        for i in range(n - 1):
            s1 = 2 * (s1 + a[i]) % MODULO

        t = s0 - s1 + a[0] - a[n - 1]
        if t < 0:
            t += MODULO

        return t


if __name__ == '__main__':
    print(Solution().sumSubseqWidths([2, 1, 3, 4]))