from functools import lru_cache


class Solution:
    def countVowelStrings(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def f(i, j):
            if i == 0:
                return 1
            r = 0
            for k in range(j + 1):
                r += f(i - 1, k)
            return r

        return f(n, 4)


if __name__ == '__main__':
    print(Solution().countVowelStrings(50))
