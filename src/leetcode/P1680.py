MOD = 10 ** 9 + 7

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        r = 0
        for i in range(1, n + 1):
            t = i.bit_length()
            r = ((r << t) + i) % MOD

        return r
