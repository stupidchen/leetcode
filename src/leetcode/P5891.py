from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        s = (n + m) * mean - sum(rolls)
        if s < 1 * n or s > 6 * n:
            return []
        k = s // n
        g = s % n
        return [k + 1] * g + [k] * (n - g)


if __name__ == '__main__':
    print(Solution().missingRolls([3, 2, 4, 3], 4, 2))
