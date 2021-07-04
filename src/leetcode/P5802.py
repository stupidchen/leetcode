MOD = 10 ** 9 + 7


class Solution:
    def countGoodNumbers(self, n: int) -> int:

        def pow(x, y):
            if y == 0:
                return 1
            t = pow(x, y >> 1)
            if y & 1 == 0:
                return t * t % MOD
            else:
                return (t * t % MOD) * x % MOD

        prime = 4
        even = 5
        return (pow(prime, n >> 1) * pow(even, n - (n >> 1))) % MOD


if __name__ == '__main__':
    print(Solution().countGoodNumbers(50))
