from collections import Counter
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c = Counter(answers)
        r = 0
        for k, v in c.items():
            t = (v - 1) // (k + 1) + 1
            r = t * (k + 1) + r
        return r


if __name__ == '__main__':
    print(Solution().numRabbits([1, 1, 2]))
