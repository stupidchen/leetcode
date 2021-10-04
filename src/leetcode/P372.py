from typing import List

MOD = 1337


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        r = 1
        for x in b:
            r = pow(r, 10) * pow(a, x) % MOD
        return r


if __name__ == '__main__':
    print(Solution().superPow(a=2, b=[1, 1]))
