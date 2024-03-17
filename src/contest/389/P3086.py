import math
from itertools import accumulate
from typing import List


class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        o = [i for i, num in enumerate(nums) if num]
        p = [0] + list(accumulate(o))
        n = len(o)
        res = math.inf
        for reserved in range(min(4, n, k) + 1):
            changes = min(k - reserved, maxChanges)
            m = k - changes

            for i in range(n - m + 1):
                mid = i + (m >> 1)
                if m & 1 == 0:
                    current = changes * 2 + p[i + m] - p[mid] - (p[mid] - p[i])
                    res = min(current, res)
                else:
                    current = changes * 2 + p[i + m] - p[mid + 1] - (p[mid] - p[i])
                    res = min(current, res)
        return res


if __name__ == '__main__':
    r = Solution().minimumMoves(nums=[0, 0, 0, 0], k=2, maxChanges=3)
    # r = Solution().minimumMoves(nums=[1] * (10 ** 5), k=1000, maxChanges=1)
    # r = Solution().minimumMoves([1, 1, 0, 0, 0, 1, 1, 0, 0, 1], 3, 1)
    # r = Solution().minimumMoves([1, 0, 1, 0, 1], 3, 0)
    # r = Solution().minimumMoves([0, 1], 1, 4)
    # r = Solution().minimumMoves([0, 1, 1], 2, 0)
    print(r)
