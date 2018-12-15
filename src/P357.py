from functools import lru_cache


class Solution:
    @lru_cache()
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = self.countNumbersWithUniqueDigits
        if n > 10:
            n = 10
        if n == 0:
            return 1
        elif n == 1:
            return 10
        else:
            return f(n - 1) + (f(n - 1) - f(n - 2)) * (10 - n + 1)
