from collections import Counter
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        c = Counter()
        r = 0
        for x, y in dominoes:
            r += c[(x, y)]
            if x != y:
                r += c[(y, x)]
            c[(y, x)] += 1

        return r


if __name__ == '__main__':
    print(Solution().numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6]]))
