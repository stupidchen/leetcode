MODULO = 10 ** 9 + 7

from math import gcd


class Solution:
    def nthMagicalNumber(self, N, A, B):
        L = A // gcd(A, B) * B

        def magicalIndex(x):
            return x // A + x // B - x // L

        l = 0
        r = 10 ** 15
        while l < r:
            mid = (l + r) >> 1
            if magicalIndex(mid) < N:
                l = mid + 1
            else:
                r = mid
        return l % MODULO


if __name__ == '__main__':
    print(Solution().nthMagicalNumber(1, 2, 2))
