from math import sqrt

MOD = 10 ** 9 + 7


class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        c = 0
        for i in range(2, n + 1):
            d = False
            for j in range(2, int(sqrt(i) + 1)):
                if i % j == 0:
                    d = True
                    break
            if not d:
                c += 1
        r = 1
        for i in range(c):
            r = ((i + 1) * r) % MOD
        for i in range(n - c):
            r = ((i + 1) * r) % MOD

        return r


if __name__ == '__main__':
    print(Solution().numPrimeArrangements(2))
