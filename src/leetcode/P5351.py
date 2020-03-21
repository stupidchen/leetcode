from functools import lru_cache


class Solution:
    def maxSizeSlices(self, slices):
        n = len(slices)

        @lru_cache(maxsize=None)
        def solve1(i, j):
            if i < 0 or j <= 0:
                return 0

            return max(solve1(i - 1, j), solve1(i - 2, j - 1) + slices[i])

        @lru_cache(maxsize=None)
        def solve2(i, j):
            if i < 1 or j <= 0:
                return 0

            return max(solve2(i - 1, j), solve2(i - 2, j - 1) + slices[i])

        t1 = max(solve1(i, n // 3) for i in range(n - 1))
        t2 = max(solve2(i, n // 3) for i in range(1, n))

        return max(t1, t2)


if __name__ == '__main__':
    print(Solution().maxSizeSlices([9, 5, 1, 7, 8, 4, 4, 5, 5, 8, 7, 7]))
