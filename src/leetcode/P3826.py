from functools import lru_cache


@lru_cache(maxsize=None)
def f(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return f(n - 1) + f(n - 2)


class Solution:
    def findIntegers(self, n: int) -> int:
        if n < 0:
            return 0

        l = n.bit_length()
        if n == (1 << l) - 1:
            return f(l)

        ret = f(l - 1)
        if n | (1 << l - 2) == n:
            ret += f(l - 2)
        else:
            ret += self.findIntegers(n & ((1 << l - 2) - 1))

        return ret


if __name__ == '__main__':
    print(Solution().findIntegers(4))
