from functools import lru_cache


class Solution:
    def stoneGameVII(self, stones):
        n = len(stones)
        s = [0] * (n + 1)
        for i, v in enumerate(stones):
            s[i + 1] = s[i] + v

        def range_sum(left, right):
            return s[right + 1] - s[left]

        @lru_cache(maxsize=3000)
        def f(left, right, round):
            if left >= right:
                return 0

            next_round = not round
            if round:
                return max(f(left + 1, right, next_round) + range_sum(left + 1, right),
                           f(left, right - 1, next_round) + range_sum(left, right - 1))
            else:
                return min(f(left + 1, right, next_round) - range_sum(left + 1, right),
                           f(left, right - 1, next_round) - range_sum(left, right - 1))

        return f(0, n - 1, True)