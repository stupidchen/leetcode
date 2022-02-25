from functools import lru_cache
from typing import List


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)

        @lru_cache(maxsize=None)
        def f(l, r):
            if l + 1 == r:
                return arr[l]
            elif l < r:
                t = float('inf')
                for i in range(l + 1, r):
                    t = min(f(l, i) + f(i, r) + max(arr[l: i]) * max(arr[i: r]), t)
                return t
            else:
                return 0

        return f(0, n) - sum(arr)


if __name__ == '__main__':
    print(Solution().mctFromLeafValues([6, 2, 4]))
