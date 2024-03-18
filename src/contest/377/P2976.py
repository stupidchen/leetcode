import math
from collections import defaultdict
from typing import List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        chars = set(original) | set(changed)
        d = defaultdict(lambda: defaultdict(lambda: math.inf))
        for cc in zip(original, changed, cost):
            x, y, w = cc
            d[x][y] = min(w, d[x][y])
        for c in chars:
            d[c][c] = 0

        for k in chars:
            for i in chars:
                for j in chars:
                    if d[i][k] + d[k][j] < d[i][j]:
                        d[i][j] = d[i][k] + d[k][j]

        res = 0
        for cc in zip(source, target):
            sc, tc = cc
            if math.isinf(d[sc][tc]):
                return -1
            res += d[sc][tc]
        return res


if __name__ == '__main__':
    r = Solution().minimumCost(source="abcd", target="abcd", original=["a", "b", "c", "c", "e", "d"],
                               changed=["b", "c", "b", "e", "b", "e"], cost=[2, 5, 5, 1, 2, 20])
    print(r)
