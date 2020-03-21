from functools import lru_cache


@lru_cache(maxsize=None)
def power(i):
    if i == 1:
        return 0
    if i & 1 == 0:
        return power(i >> 1) + 1
    else:
        return power(3 * i + 1) + 1


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        a = sorted([i for i in range(lo, hi + 1)], key=lambda x: (power(x), x))
        return a[k - 1]


if __name__ == '__main__':
    print(Solution().getKth(lo=1, hi=1000, k=777))
