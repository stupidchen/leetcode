from functools import lru_cache


@lru_cache()
def f(n, t):
    if n == 1:
        return 1
    ret = 0
    if t:
        ret = n
    ret = max(ret, max([f(i, True) * (n - i) for i in range(1, n)]))
    return ret


class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        return f(n, False)


if __name__ == '__main__':
    print(Solution().integerBreak(5))
